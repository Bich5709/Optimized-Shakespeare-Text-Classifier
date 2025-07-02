# Unique Words Part 1: Optimize the Classifier

## Overview

This project involves developing and optimizing a simple text classification algorithm to determine whether a given text fragment was written by William Shakespeare. The classifier works by measuring how many **unique words** from a predefined list of Shakespearean vocabulary appear in a given text fragment.

The project emphasizes **performance optimization**, specifically improving the runtime of the classification algorithm by reducing its time complexity from **O(N²)** to **O(N)**.

---

## Problem Statement

Given a list of words typically used by Shakespeare and a collection of text fragments, the goal is to:

- Calculate a **Shakespeare score** for each fragment.
- Classify each fragment as **Shakespearean** or **not**, based on a threshold.
- Optimize the algorithm's performance using efficient data structures (e.g., sets).

---

## Shakespeare Score

The Shakespeare score is calculated as:

