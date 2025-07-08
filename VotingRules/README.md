# Voting Rules Implementation – COMP517 Coursework

This project was developed as part of COMP517 in the MSc Data Science and AI program at the University of Liverpool. It focuses on implementing fundamental voting rules in computational social choice theory using Python.

## Voting Rules Implemented

- **Dictatorship** – Selects the top-ranked candidate of a designated agent.
- **Scoring Rule** – Applies a score vector across rankings, with tie-breaking.
- **Plurality** – Awards one point to each voter's top-ranked candidate.
- **Veto** – Removes each voter's least-preferred candidate from scoring.
- **Borda Count** – Assigns decreasing scores from top to bottom rank.
- **STV (Single Transferable Vote)** – Repeatedly eliminates the least-preferred candidates until one remains.

Each rule includes error handling and deterministic tie-breaking logic based on a designated agent's preference.

## System Design

A `Preference` class is provided with the following interface:

- `candidates()` – Returns a list of all candidates.
- `voters()` – Returns a list of voter IDs.
- `get_preference(candidate, voter)` – Returns the rank (0 = highest) that a voter assigns to a candidate.

Each voting rule function queries this interface and is written in a modular style to facilitate testing and reuse.

## Tools and Skills

- **Language**: Python 3
- **Libraries**: None required (pure Python implementation)
- **Skills**: Algorithmic design, social choice theory, ranking systems, test-driven development

## License and Disclaimer

This project was submitted as part of assessed coursework and is intended for educational and portfolio use only. **Do not copy, reuse, or submit this code for academic credit elsewhere.**

## Attribution

- **Module**: COMP517
- **Program**: MSc Data Science and AI
- **Institution**: University of Liverpool
- **Author**: Jintaek Uh
- © 2025 Jintaek Uh
