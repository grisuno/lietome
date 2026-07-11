# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 1 | **Total Symbols Extracted:** 0 | **Total Imports:** 4

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    main_py["main.py (py)"]
    class main_py mod;
    ext_pygame["pygame"]
    class ext_pygame ext;
    main_py -.->|imports| ext_pygame
    ext_sys["sys"]
    class ext_sys ext;
    main_py -.->|imports| ext_sys
    ext_random["random"]
    class ext_random ext;
    main_py -.->|imports| ext_random
    ext_pygame_locals["pygame.locals"]
    class ext_pygame_locals ext;
    main_py -.->|imports| ext_pygame_locals
```

---

## Architecture Reference

### PY (1 files)

#### `main.py`
**Path:** `main.py`

*No symbols extracted*
