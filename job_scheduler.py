import heapq

class JobScheduler:
    """
    Min‑heap priority queue for jobs.
    - add_job: O(log n)
    - process_next: O(log n)
    - peek_next: O(1)
    """
    def __init__(self):
        self.heap = []          # (priority, counter, description)
        self.counter = 0        # tie‑breaker (FIFO for same priority)

    def add_job(self, priority: int, description: str):
        self.counter += 1
        heapq.heappush(self.heap, (priority, self.counter, description))
        print(f"✅ Added: [{description}] with priority {priority}")

    def process_next(self):
        if not self.heap:
            print("⚠️ No jobs in queue.")
            return None
        priority, _, desc = heapq.heappop(self.heap)
        print(f"⚙️ Processing: [{desc}] (priority {priority})")
        return desc

    def peek_next(self):
        if not self.heap:
            print("📭 Queue is empty.")
            return None
        priority, _, desc = self.heap[0]
        print(f"👀 Next job: [{desc}] (priority {priority})")
        return desc

    def pending_count(self) -> int:
        count = len(self.heap)
        print(f"📊 Pending jobs: {count}")
        return count

    def list_all(self):
        if not self.heap:
            print("📭 No pending jobs.")
            return
        print("📋 Pending jobs (unsorted):")
        # Show in heap order (not sorted by priority – that's the point)
        for priority, _, desc in self.heap:
            print(f"   - Priority {priority}: {desc}")

# ---------- Demo ----------
if __name__ == "__main__":
    s = JobScheduler()
    print("=== Job Scheduler Simulator ===\n")
    s.add_job(3, "Send welcome email")
    s.add_job(1, "Charge credit card")
    s.add_job(5, "Update analytics")
    s.add_job(1, "Verify payment")
    s.pending_count()
    s.peek_next()
    print("\n--- Processing ---")
    s.process_next()   # priority 1, "Charge credit card"
    s.process_next()   # priority 1, "Verify payment"
    s.process_next()   # priority 3
    s.process_next()   # priority 5
    s.process_next()   # empty
    print("\n--- Later high priority job ---")
    s.add_job(0, "Refund customer")
    s.peek_next()
    s.process_next()