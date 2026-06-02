# ⚡ Job Scheduler Simulator – Heap (Priority Queue)

> **Day 2 of DSA in Production**
> Understanding how Heaps power real-world schedulers, task queues, and priority-based systems.

## 🚀 Overview

This project is a lightweight **Job Scheduler Simulator** built using a **Min Heap (Priority Queue)**.

The scheduler always executes the highest-priority job first without scanning the entire list of jobs.

It demonstrates how priority queues are used in real production systems such as:

* Operating System CPU Schedulers
* Ride Matching Platforms
* Background Task Queues
* Network Packet Scheduling
* Event Processing Systems

---

## 🎯 The Problem

Imagine a system with thousands of pending jobs:

* Send welcome email
* Verify payment
* Generate invoice
* Process refund

How do we always pick the most important job efficiently?

### Naive Approach

Store jobs in a list and scan for the highest priority every time.

**Time Complexity:** O(n)

For 1,000,000 jobs, that means potentially scanning 1,000,000 entries for every execution.

### Heap-Based Approach

Store jobs in a Min Heap.

* Insert → O(log n)
* Remove Highest Priority → O(log n)
* Peek Highest Priority → O(1)

This is exactly how many production schedulers work internally.

---

## 🏗️ Project Structure

```text
.
├── job_scheduler.py
├── app.py
├── requirements.txt
└── README.md
```

### Files

| File             | Purpose                         |
| ---------------- | ------------------------------- |
| job_scheduler.py | Core heap implementation        |
| app.py           | Interactive Streamlit dashboard |
| requirements.txt | Dependencies                    |
| README.md        | Project documentation           |

---

## 🧠 DSA Concept Used

### Heap (Priority Queue)

A Min Heap is a binary tree where the smallest element always stays at the root.

In this project:

```text
Lower Number = Higher Priority
```

Example:

```text
Priority 0 → Critical
Priority 1 → High
Priority 3 → Medium
Priority 5 → Low
```

Heap Structure:

```text
        0
      /   \
     1     3
    /
   5
```

The next job to execute is always available at the root.

---

## ⚙️ Operations Supported

| Operation     | Complexity |
| ------------- | ---------- |
| Add Job       | O(log n)   |
| Process Job   | O(log n)   |
| Peek Next Job | O(1)       |
| Count Jobs    | O(1)       |
| View Queue    | O(n)       |

---

## ▶️ Running the Project

### Option 1: Command Line Version

```bash
python job_scheduler.py
```

### Sample Output

```text
=== Job Scheduler Simulator ===

Added: Send welcome email (Priority 3)
Added: Charge credit card (Priority 1)
Added: Update analytics (Priority 5)
Added: Verify payment (Priority 1)

Next Job:
Charge credit card

Processing...

Charge credit card
Verify payment
Send welcome email
Update analytics
```

---

### Option 2: Streamlit Dashboard

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🌍 Real-World Applications

### Operating Systems

CPU schedulers use priorities to determine which process should run next.

### Ride Matching Platforms

High-priority requests can be matched before normal requests.

### Task Queues

Systems such as Celery and RabbitMQ support priority-based job execution.

### Networking

Routers prioritize critical packets over less important traffic.

### Graph Algorithms

Dijkstra's Algorithm uses a Priority Queue to efficiently determine shortest paths.

---

## 📈 Why Heaps Matter

Without a heap:

```text
Find highest priority → O(n)
```

With a heap:

```text
Insert → O(log n)
Remove Highest Priority → O(log n)
Peek → O(1)
```

For large-scale systems, this difference becomes significant.

---

## 🔄 Future Enhancements

### 1. Delayed Job Scheduling

Execute jobs only after a specific timestamp.

Example:

```python
(timestamp, priority, job)
```

Useful for reminders, notifications, and cron-like systems.

---

### 2. Retry Mechanism

Failed jobs automatically re-enter the queue.

```text
Attempt 1
Attempt 2
Attempt 3
Dead Letter Queue
```

Common in production task-processing systems.

---

### 3. Priority Aging

Increase the priority of long-waiting jobs to prevent starvation.

This ensures fairness across the system.

---

### 4. Redis-Based Distributed Queue

Replace the in-memory heap with Redis Sorted Sets.

Benefits:

* Shared across multiple servers
* Survives restarts
* Horizontally scalable

## 🐛 Current Limitations

* In-memory storage only
* No persistence
* Single-threaded
* No distributed workers

These limitations are intentional to keep the project focused on learning the Heap data structure.

---

## 🎓 Key Takeaways

* Heaps provide efficient priority-based scheduling.
* Insertions and removals are logarithmic.
* Priority Queues appear frequently in interviews and production systems.
* Understanding Heaps bridges the gap between DSA and system design.

---

## 👨‍💻 Author

**Susmit Naskar**

GitHub: https://github.com/Nas-Susmit

Part of the **DSA in Production** series where each project demonstrates how a classic DSA concept is used in real-world software systems.

### Day 1

HashMap → Login Session Manager

### Day 2

Heap → Job Scheduler Simulator

---

⭐ If this project helped you understand Heaps better, consider giving the repository a star.
