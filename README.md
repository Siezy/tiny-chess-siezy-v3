# tiny-chess v3

Maxed-out 4 KB engine: 0x88 board, negamax with alpha-beta + iterative
deepening, transposition table, killer moves, check extensions, quiescence
with check evasions, MVV + killer + TT-move ordering, piece-square eval,
fixed node budget (never a clock, so live and replay agree).
Standard library only.
