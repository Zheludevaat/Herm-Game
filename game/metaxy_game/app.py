from __future__ import annotations

from pathlib import Path

import pygame

from .codex import unlocked_entries
from .config import CFG, PALETTE
from .dialogue import INQUIRY_OPTIONS, resolve_choice
from .endings import ending_label, evaluate_ending
from .level import Level
from .narrative import CALLING_INTROS, CALLINGS, GUARDIAN_RITUAL_LINES
from .player import Player
from .art import draw_backdrop, marker_sprite, npc_sprite, player_sprite, tile_surface
from .progression import ACTS, next_act_name
from .quest import (
    completed_side_quests_for_level,
    mark_spoken_in_level,
    mark_trial_passed,
    objective_line,
    relic_collected_for_level,
    relic_for_level,
    spoken_in_level,
    trial_passed_in_level,
)
from .save import load_game, save_game
from .state import SoulState
from .verbs import VERBS, apply_verb

LEVEL_ORDER = tuple(str(act["name"]) for act in ACTS)
LEVEL_PATHS = {str(act["name"]): str(act["file"]) for act in ACTS}
LEVEL_LABELS = {str(act["name"]): str(act["label"]) for act in ACTS}
LEVEL_GOALS = {str(act["name"]): dict(act["goal"]) for act in ACTS}
LEVEL_DIALOGUE_HINTS = {str(act["name"]): str(act["dialogue_hint"]) for act in ACTS}
LEVEL_RELICS = {str(act["name"]): str(act["relic"]) for act in ACTS}


def load_level(name: str) -> Level:
    level_path = Path(__file__).resolve().parents[1] / "data" / LEVEL_PATHS[name]
    return Level.from_json(level_path)


def build_level_context(level: Level) -> dict[str, set[tuple[int, int]]]:
    return {
        "memory_shards": set(level.find_markers("M")),
        "dissonance_zones": set(level.find_markers("X")),
        "thresholds": set(level.find_markers("T")),
        "harmony_shrines": set(level.find_markers("H")),
        "side_quest_nodes": set(level.find_markers("Q")),
        "trial_nodes": set(level.find_markers("G")),
        "relic_nodes": set(level.find_markers("R")),
    }


def draw_level(surface: pygame.Surface, level: Level, level_name: str) -> None:
    tile = level.tile_size
    for y, row in enumerate(level.grid):
        for x, cell in enumerate(row):
            kind = "wall" if cell == "#" else "floor"
            variant = (x + y) % 3
            tile_img = tile_surface(level_name, kind, tile, variant)
            surface.blit(tile_img, (x * tile, y * tile))


def ui_font(state: SoulState) -> pygame.font.Font:
    return pygame.font.Font(None, state.ui_font_size)


def ui_text_color(state: SoulState) -> tuple[int, int, int]:
    return PALETTE["accent"] if state.high_contrast else PALETTE["bg3"]


def draw_hud(surface: pygame.Surface, state: SoulState, message: str, level_name: str) -> None:
    font = ui_font(state)
    text_color = ui_text_color(state)
    hud_bg = pygame.Rect(0, 0, CFG.logical_width, 20)
    pygame.draw.rect(surface, PALETTE["bg1"], hud_bg)

    coherence = font.render(f"Coh:{state.coherence}", True, text_color)
    clarity = font.render(f"Clr:{state.clarity}", True, text_color)
    shards = font.render(f"Mem:{state.memory_shards}", True, text_color)
    relics = font.render(f"Rlc:{len(state.relics_collected)}", True, text_color)
    zone = font.render(f"Zone:{LEVEL_LABELS[level_name]}", True, text_color)
    surface.blit(coherence, (4, 4))
    surface.blit(clarity, (48, 4))
    surface.blit(shards, (88, 4))
    surface.blit(relics, (120, 4))
    surface.blit(zone, (154, 4))

    if message:
        msg = font.render(message[:40], True, text_color)
        surface.blit(msg, (4, CFG.logical_height - 12))


def draw_dialogue_wheel(surface: pygame.Surface, selected: int, state: SoulState) -> None:
    font = ui_font(state)
    text_color = ui_text_color(state)
    box = pygame.Rect(8, 26, CFG.logical_width - 16, CFG.logical_height - 40)
    pygame.draw.rect(surface, PALETTE["bg0"], box)
    pygame.draw.rect(surface, PALETTE["bg3"], box, 1)

    title = font.render("Inquiry Wheel (1-7, Enter)", True, text_color)
    surface.blit(title, (12, 30))

    for i, option in enumerate(INQUIRY_OPTIONS):
        prefix = ">" if i == selected else " "
        line = font.render(f"{prefix} {i + 1}. {option}", True, text_color)
        surface.blit(line, (12, 44 + i * 12))


def draw_codex(surface: pygame.Surface, state: SoulState) -> None:
    font = ui_font(state)
    text_color = ui_text_color(state)
    box = pygame.Rect(6, 24, CFG.logical_width - 12, CFG.logical_height - 30)
    pygame.draw.rect(surface, PALETTE["bg0"], box)
    pygame.draw.rect(surface, PALETTE["bg3"], box, 1)
    surface.blit(font.render("Codex (C to close)", True, text_color), (10, 28))

    for i, line in enumerate(unlocked_entries(state)):
        surface.blit(font.render(f"- {line}", True, text_color), (10, 42 + i * 12))


def draw_victory_panel(surface: pygame.Surface, state: SoulState) -> None:
    font = ui_font(state)
    text_color = ui_text_color(state)
    box = pygame.Rect(10, 26, CFG.logical_width - 20, CFG.logical_height - 52)
    pygame.draw.rect(surface, PALETTE["bg0"], box)
    pygame.draw.rect(surface, PALETTE["accent"], box, 1)
    lines = [
        "METAXY chapter set complete",
        f"Clarity: {state.clarity}",
        f"Memory: {state.memory_shards}",
        f"Ending: {ending_label(state.final_ending)}",
        "F5 save, R restart, ESC quit",
    ]
    for i, line in enumerate(lines):
        surface.blit(font.render(line, True, text_color), (16, 34 + i * 12))


def draw_prologue_panel(surface: pygame.Surface, selected: int, state: SoulState) -> None:
    font = ui_font(state)
    text_color = ui_text_color(state)
    box = pygame.Rect(8, 20, CFG.logical_width - 16, CFG.logical_height - 24)
    pygame.draw.rect(surface, PALETTE["bg0"], box)
    pygame.draw.rect(surface, PALETTE["bg3"], box, 1)
    surface.blit(font.render("Choose mortal calling (1-3)", True, text_color), (12, 24))
    for idx, calling in enumerate(CALLINGS):
        prefix = ">" if idx == selected else " "
        surface.blit(font.render(f"{prefix} {idx + 1}. {calling}", True, text_color), (12, 38 + idx * 12))
    line = CALLING_INTROS[CALLINGS[selected]]
    surface.blit(font.render(line[:40], True, text_color), (12, 86))
    surface.blit(font.render("ENTER to confirm", True, text_color), (12, 98))


def draw_reception_panel(surface: pygame.Surface, ritual_step: int, state: SoulState) -> None:
    font = ui_font(state)
    text_color = ui_text_color(state)
    box = pygame.Rect(8, 24, CFG.logical_width - 16, CFG.logical_height - 30)
    pygame.draw.rect(surface, PALETTE["bg0"], box)
    pygame.draw.rect(surface, PALETTE["accent"], box, 1)
    surface.blit(font.render("Reception Ritual", True, text_color), (12, 28))
    for idx in range(ritual_step + 1):
        surface.blit(font.render(GUARDIAN_RITUAL_LINES[idx][:40], True, text_color), (12, 44 + idx * 12))
    surface.blit(font.render("ENTER to continue", True, text_color), (12, 112))


def draw_accessibility_panel(surface: pygame.Surface, state: SoulState) -> None:
    font = ui_font(state)
    text_color = ui_text_color(state)
    box = pygame.Rect(12, 28, CFG.logical_width - 24, CFG.logical_height - 40)
    pygame.draw.rect(surface, PALETTE["bg0"], box)
    pygame.draw.rect(surface, PALETTE["accent"], box, 1)
    lines = [
        "Accessibility (F1 to close)",
        f"H: High Contrast {'ON' if state.high_contrast else 'OFF'}",
        f"R: Reduced Flash {'ON' if state.reduced_flash else 'OFF'}",
        f"+/-: UI Font Size {state.ui_font_size}",
    ]
    for i, line in enumerate(lines):
        surface.blit(font.render(line, True, text_color), (16, 34 + i * 12))


def set_level_progress_completed(level_name: str, state: SoulState) -> None:
    field_name = f"{level_name.split('_')[0]}_completed"
    if hasattr(state, field_name):
        setattr(state, field_name, True)


def run() -> None:
    pygame.init()
    pygame.display.set_caption(CFG.title)

    window = pygame.display.set_mode((CFG.window_width, CFG.window_height))
    logical = pygame.Surface((CFG.logical_width, CFG.logical_height))

    current_level = "moon_threshold"
    level = load_level(current_level)
    spawn = tuple(float(v) for v in (level.spawn_point or (40, 40)))
    level_contexts = {name: build_level_context(load_level(name)) for name in LEVEL_ORDER}

    player = Player(x=spawn[0], y=spawn[1])
    state = SoulState()

    loaded = load_game()
    if loaded:
        player_data, loaded_state, loaded_level = loaded
        player.x = float(player_data.get("x", player.x))
        player.y = float(player_data.get("y", player.y))
        state = loaded_state
        if loaded_level in LEVEL_PATHS:
            current_level = loaded_level
            level = load_level(current_level)
            spawn = tuple(float(v) for v in (level.spawn_point or (40, 40)))
        else:
            player.x, player.y = spawn

    def refresh_level_context() -> tuple[
        set[tuple[int, int]],
        set[tuple[int, int]],
        set[tuple[int, int]],
        set[tuple[int, int]],
        set[tuple[int, int]],
        set[tuple[int, int]],
        set[tuple[int, int]],
    ]:
        ctx = level_contexts[current_level]
        return (
            set(ctx["memory_shards"]),
            set(ctx["dissonance_zones"]),
            set(ctx["thresholds"]),
            set(ctx["harmony_shrines"]),
            set(ctx["side_quest_nodes"]),
            set(ctx["trial_nodes"]),
            set(ctx["relic_nodes"]),
        )

    npc_pos = tuple(float(v) for v in (level.npc_point or (112, 56)))
    memory_shards, dissonance_zones, thresholds, harmony_shrines, side_quest_nodes, trial_nodes, relic_nodes = refresh_level_context()
    if relic_collected_for_level(current_level, state):
        relic_nodes.clear()

    in_dialogue = False
    codex_open = False
    selected_option = 0
    selected_calling = 0
    ritual_step = 0
    active_verb_index = 0
    game_mode = "play"
    accessibility_open = False
    trial_active = False
    trial_focus = 0.0
    trial_target = 2.5
    message = "Reach resident (E), Codex C"
    game_complete = state.mars_completed

    if not state.calling:
        game_mode = "prologue"
    elif not state.reception_complete:
        game_mode = "reception"

    clock = pygame.time.Clock()
    running = True
    dissonance_tick = 0.0

    while running:
        dt = clock.tick(CFG.target_fps) / 1000.0
        near_threshold = any(abs(player.x - t[0]) < 10 and abs(player.y - t[1]) < 10 for t in thresholds)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    accessibility_open = not accessibility_open
                    message = "Accessibility open" if accessibility_open else "Accessibility closed"
                    continue

                if accessibility_open:
                    if event.key == pygame.K_h:
                        state.high_contrast = not state.high_contrast
                    elif event.key == pygame.K_r:
                        state.reduced_flash = not state.reduced_flash
                    elif event.key in (pygame.K_EQUALS, pygame.K_PLUS):
                        state.cycle_font_size(1)
                    elif event.key == pygame.K_MINUS:
                        state.cycle_font_size(-1)
                    continue

                if trial_active:
                    if event.key == pygame.K_ESCAPE:
                        trial_active = False
                        trial_focus = 0.0
                        message = "Trial canceled"
                    continue

                if game_mode == "prologue":
                    if pygame.K_1 <= event.key <= pygame.K_3:
                        selected_calling = event.key - pygame.K_1
                    elif event.key == pygame.K_UP:
                        selected_calling = (selected_calling - 1) % len(CALLINGS)
                    elif event.key == pygame.K_DOWN:
                        selected_calling = (selected_calling + 1) % len(CALLINGS)
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        state.calling = CALLINGS[selected_calling]
                        message = f"Calling chosen: {state.calling}"
                        game_mode = "reception"
                    continue

                if game_mode == "reception":
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        ritual_step += 1
                        if ritual_step >= len(GUARDIAN_RITUAL_LINES):
                            state.reception_complete = True
                            game_mode = "play"
                            ritual_step = len(GUARDIAN_RITUAL_LINES) - 1
                            message = "Reception complete. Begin ascent."
                    continue

                if event.key == pygame.K_c:
                    codex_open = not codex_open
                    message = "Codex open" if codex_open else "Codex closed"
                if event.key == pygame.K_TAB and not (in_dialogue or codex_open):
                    active_verb_index = (active_verb_index + 1) % len(VERBS)
                    message = f"Active verb: {VERBS[active_verb_index].name}"
                if event.key == pygame.K_f and not (in_dialogue or codex_open):
                    message = apply_verb(state, VERBS[active_verb_index], context="traversal")

                if event.key == pygame.K_F5:
                    save_game(player, state, current_level)
                    message = "Saved"
                elif event.key == pygame.K_F9:
                    loaded = load_game()
                    if loaded:
                        player_data, loaded_state, loaded_level = loaded
                        player.x = float(player_data.get("x", player.x))
                        player.y = float(player_data.get("y", player.y))
                        state = loaded_state
                        game_complete = state.mars_completed
                        if loaded_level in LEVEL_PATHS:
                            current_level = loaded_level
                            level = load_level(current_level)
                            spawn = tuple(float(v) for v in (level.spawn_point or (40, 40)))
                            npc_pos = tuple(float(v) for v in (level.npc_point or (112, 56)))
                            memory_shards, dissonance_zones, thresholds, harmony_shrines, side_quest_nodes, trial_nodes, relic_nodes = refresh_level_context()
                            if relic_collected_for_level(current_level, state):
                                relic_nodes.clear()
                        message = "Loaded"

                if near_threshold and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    goals = LEVEL_GOALS[current_level]
                    goal_met = (
                        state.clarity >= int(goals["clarity"])
                        and state.memory_shards >= int(goals["memory_shards"])
                        and (not bool(goals["spoken"]) or spoken_in_level(current_level, state))
                        and completed_side_quests_for_level(current_level, state) >= int(goals["side_quests"])
                        and relic_collected_for_level(current_level, state)
                        and (not bool(goals.get("trial", False)) or trial_passed_in_level(current_level, state))
                    )

                    if goal_met:
                        set_level_progress_completed(current_level, state)
                        next_level = next_act_name(current_level)
                        if next_level:
                            current_level = next_level
                            level = load_level(current_level)
                            spawn = tuple(float(v) for v in (level.spawn_point or (40, 40)))
                            npc_pos = tuple(float(v) for v in (level.npc_point or (112, 56)))
                            memory_shards, dissonance_zones, thresholds, harmony_shrines, side_quest_nodes, trial_nodes, relic_nodes = refresh_level_context()
                            if relic_collected_for_level(current_level, state):
                                relic_nodes.clear()
                            player.x, player.y = spawn
                            message = f"{LEVEL_LABELS[current_level]} entered."
                        else:
                            state.final_ending = evaluate_ending(state)
                            game_complete = True
                            message = f"Final threshold complete. {ending_label(state.final_ending)}."
                    else:
                        message = (
                            f"Need Talk+Clr>={goals['clarity']}+Mem>={goals['memory_shards']}"
                        )

                if event.key == pygame.K_r and game_complete:
                    state = SoulState()
                    current_level = "moon_threshold"
                    level = load_level(current_level)
                    spawn = tuple(float(v) for v in (level.spawn_point or (40, 40)))
                    npc_pos = tuple(float(v) for v in (level.npc_point or (112, 56)))
                    memory_shards, dissonance_zones, thresholds, harmony_shrines, side_quest_nodes, trial_nodes, relic_nodes = refresh_level_context()
                    if relic_collected_for_level(current_level, state):
                        relic_nodes.clear()
                    player.x, player.y = spawn
                    game_complete = False
                    message = "Journey reset"

                if not (in_dialogue or codex_open) and event.key == pygame.K_e:
                    near_trial = any(abs(player.x - g[0]) < 10 and abs(player.y - g[1]) < 10 for g in trial_nodes)
                    if near_trial and not trial_passed_in_level(current_level, state):
                        trial_active = True
                        trial_focus = 0.0
                        message = "Governor trial: hold S to center"

                    near_shrine = any(abs(player.x - h[0]) < 10 and abs(player.y - h[1]) < 10 for h in harmony_shrines)
                    if near_shrine:
                        state.recover_coherence(20)
                        message = "Harmony restored (+20 Coherence)"

                    near_side_quest = {q for q in side_quest_nodes if abs(player.x - q[0]) < 10 and abs(player.y - q[1]) < 10}
                    if near_side_quest:
                        for q in near_side_quest:
                            quest_id = f"{current_level}:{q[0]}:{q[1]}"
                            if state.complete_side_quest(quest_id):
                                state.gain_clarity(1)
                                message = "Side quest insight completed (+1 Clarity)"
                    near_relic = {r for r in relic_nodes if abs(player.x - r[0]) < 10 and abs(player.y - r[1]) < 10}
                    if near_relic:
                        relic_name = relic_for_level(current_level)
                        if state.collect_relic(relic_name):
                            state.gain_clarity(1)
                            for r in near_relic:
                                relic_nodes.discard(r)
                            message = f"Recovered relic: {relic_name}"
                        else:
                            message = f"Relic already integrated: {relic_name}"

                    if abs(player.x - npc_pos[0]) < 14 and abs(player.y - npc_pos[1]) < 14:
                        in_dialogue = True
                        message = LEVEL_DIALOGUE_HINTS[current_level]

                if in_dialogue:
                    if pygame.K_1 <= event.key <= pygame.K_7:
                        selected_option = event.key - pygame.K_1
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        result = resolve_choice(selected_option, state, current_level)
                        mark_spoken_in_level(current_level, state)
                        message = result.line
                        in_dialogue = False
                    elif event.key == pygame.K_ESCAPE:
                        in_dialogue = False
                        message = "Dialogue closed"

        if game_mode == "play" and not (in_dialogue or codex_open or game_complete or accessibility_open or trial_active):
            keys = pygame.key.get_pressed()
            dx = (1 if keys[pygame.K_RIGHT] or keys[pygame.K_d] else 0) - (
                1 if keys[pygame.K_LEFT] or keys[pygame.K_a] else 0
            )
            dy = (1 if keys[pygame.K_DOWN] or keys[pygame.K_s] else 0) - (
                1 if keys[pygame.K_UP] or keys[pygame.K_w] else 0
            )
            player.move(dx, dy, dt, level.is_blocked)

        if trial_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                trial_focus = min(trial_target, trial_focus + dt)
            else:
                trial_focus = max(0.0, trial_focus - dt * 0.75)

            if trial_focus >= trial_target:
                trial_active = False
                trial_focus = 0.0
                mark_trial_passed(current_level, state)
                state.gain_clarity(2)
                state.recover_coherence(10)
                message = "Governor trial passed (+2 Clarity)"

        collected = {s for s in memory_shards if abs(player.x - s[0]) < 8 and abs(player.y - s[1]) < 8}
        if collected:
            for shard in collected:
                memory_shards.remove(shard)
                state.gain_memory_shard()
            message = "Recovered memory shard"

        in_dissonance = any(abs(player.x - z[0]) < 8 and abs(player.y - z[1]) < 8 for z in dissonance_zones)
        dissonance_tick += dt
        dissonance_interval = 0.5 if state.reduced_flash else 0.2
        if in_dissonance and not (in_dialogue or codex_open or accessibility_open) and dissonance_tick >= dissonance_interval:
            state.lose_coherence(1)
            dissonance_tick = 0.0
            message = "Dissonance encounter"

        if state.coherence <= 0:
            player.x, player.y = spawn
            state.coherence = 60
            message = "Obscured. Returned to last clarity."

        frame = (pygame.time.get_ticks() // 240) % 2
        draw_backdrop(logical, current_level, frame)
        draw_level(logical, level, current_level)

        for shard in memory_shards:
            icon = marker_sprite(current_level, "memory", frame)
            logical.blit(icon, (shard[0] - icon.get_width() / 2, shard[1] - icon.get_height() / 2))

        for zone in dissonance_zones:
            icon = marker_sprite(current_level, "dissonance", frame)
            logical.blit(icon, (zone[0] - icon.get_width() / 2, zone[1] - icon.get_height() / 2))

        for threshold in thresholds:
            icon = marker_sprite(current_level, "threshold", frame)
            logical.blit(icon, (threshold[0] - icon.get_width() / 2, threshold[1] - icon.get_height() / 2))
        for shrine in harmony_shrines:
            icon = marker_sprite(current_level, "shrine", frame)
            logical.blit(icon, (shrine[0] - icon.get_width() / 2, shrine[1] - icon.get_height() / 2))
        for side_quest in side_quest_nodes:
            icon = marker_sprite(current_level, "side_quest", frame)
            logical.blit(icon, (side_quest[0] - icon.get_width() / 2, side_quest[1] - icon.get_height() / 2))
        for trial_node in trial_nodes:
            icon = marker_sprite(current_level, "trial", frame)
            logical.blit(icon, (trial_node[0] - icon.get_width() / 2, trial_node[1] - icon.get_height() / 2))
        for relic_node in relic_nodes:
            icon = marker_sprite(current_level, "relic", frame)
            logical.blit(icon, (relic_node[0] - icon.get_width() / 2, relic_node[1] - icon.get_height() / 2))

        p_sprite = player_sprite(current_level, frame)
        n_sprite = npc_sprite(current_level, frame)
        logical.blit(p_sprite, (player.x - p_sprite.get_width() / 2, player.y - p_sprite.get_height() / 2))
        logical.blit(n_sprite, (npc_pos[0] - n_sprite.get_width() / 2, npc_pos[1] - n_sprite.get_height() / 2))

        draw_hud(logical, state, message, current_level)
        if game_mode == "prologue":
            draw_prologue_panel(logical, selected_calling, state)
        elif game_mode == "reception":
            draw_reception_panel(logical, ritual_step, state)
        else:
            if in_dialogue:
                draw_dialogue_wheel(logical, selected_option, state)
            if codex_open:
                draw_codex(logical, state)
        if accessibility_open:
            draw_accessibility_panel(logical, state)

        if near_threshold:
            font = pygame.font.Font(None, 12)
            goals = LEVEL_GOALS[current_level]
            goal_met = (
                state.clarity >= int(goals["clarity"])
                and state.memory_shards >= int(goals["memory_shards"])
                and (not bool(goals["spoken"]) or spoken_in_level(current_level, state))
                and completed_side_quests_for_level(current_level, state) >= int(goals["side_quests"])
                and relic_collected_for_level(current_level, state)
                and (not bool(goals.get("trial", False)) or trial_passed_in_level(current_level, state))
            )
            label = "cross" if next_act_name(current_level) else "complete"
            talk_hint = "Y" if spoken_in_level(current_level, state) else "N"
            side_quest_hint = completed_side_quests_for_level(current_level, state)
            trial_hint = "Y" if trial_passed_in_level(current_level, state) else "N"
            relic_hint = "Y" if relic_collected_for_level(current_level, state) else "N"
            hint = (
                f"Press SPACE to {label}"
                if goal_met
                else f"Need T{talk_hint} R{trial_hint} L{relic_hint} SQ{side_quest_hint}/{goals['side_quests']} C{goals['clarity']} M{goals['memory_shards']}"
            )
            logical.blit(font.render(hint, True, PALETTE["bg3"]), (4, 132))
        else:
            goals = LEVEL_GOALS[current_level]
            objective = objective_line(current_level, state, int(goals["clarity"]), int(goals["memory_shards"]))
            font = pygame.font.Font(None, 12)
            logical.blit(font.render(objective[:44], True, PALETTE["bg3"]), (4, 132))

        if game_complete:
            draw_victory_panel(logical, state)

        if game_mode == "play":
            font = ui_font(state)
            verb_text = f"Verb:{VERBS[active_verb_index].name} (TAB/F)"
            logical.blit(font.render(verb_text[:30], True, ui_text_color(state)), (84, 132))

        if trial_active:
            bar_x, bar_y, bar_w, bar_h = 18, 120, 124, 10
            pygame.draw.rect(logical, PALETTE["bg0"], (bar_x, bar_y, bar_w, bar_h), 0)
            pygame.draw.rect(logical, PALETTE["bg3"], (bar_x, bar_y, bar_w, bar_h), 1)
            fill = int((trial_focus / trial_target) * (bar_w - 2))
            pygame.draw.rect(logical, PALETTE["accent"], (bar_x + 1, bar_y + 1, fill, bar_h - 2), 0)
            prompt_font = pygame.font.Font(None, 12)
            logical.blit(prompt_font.render("Hold S to remain centered", True, PALETTE["bg3"]), (18, 110))

        scaled = pygame.transform.scale(logical, (CFG.window_width, CFG.window_height))
        window.blit(scaled, (0, 0))
        pygame.display.flip()

    pygame.quit()
