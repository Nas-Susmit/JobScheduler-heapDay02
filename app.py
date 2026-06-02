import streamlit as st
import heapq
import time
from datetime import datetime

class JobScheduler:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def add_job(self, priority, description):
        self.counter += 1
        heapq.heappush(self.heap, (priority, self.counter, description, datetime.now()))

    def process_next(self):
        if not self.heap:
            return None
        priority, _, desc, _ = heapq.heappop(self.heap)
        return (priority, desc)

    def peek_next(self):
        if not self.heap:
            return None
        return self.heap[0][0], self.heap[0][2]

    def size(self):
        return len(self.heap)

    def get_all(self):
        return sorted(self.heap)   # heap order is same as sorted by (priority, counter)

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Heap Job Scheduler", page_icon="⚡")
st.title("⚡ Job Scheduler Simulator")
st.markdown("**Priority Queue (Min‑Heap)** – Every operation is **O(log n)**")

# Initialise scheduler in session state
if "scheduler" not in st.session_state:
    st.session_state.scheduler = JobScheduler()
if "log" not in st.session_state:
    st.session_state.log = []

sched = st.session_state.scheduler

# Sidebar controls
with st.sidebar:
    st.header("➕ Add a job")
    desc = st.text_input("Job description", placeholder="e.g., Process payment")
    priority = st.slider("Priority (lower = higher)", 0, 10, 5)
    if st.button("Add job", use_container_width=True):
        if desc.strip():
            sched.add_job(priority, desc)
            st.session_state.log.insert(0, f"✅ Added '{desc}' (P:{priority})")
            st.rerun()
        else:
            st.warning("Please enter a description")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Process next", use_container_width=True):
            job = sched.process_next()
            if job:
                st.session_state.log.insert(0, f"⚙️ Processed '{job[1]}' (P:{job[0]})")
            else:
                st.session_state.log.insert(0, "📭 No jobs to process")
            st.rerun()
    with col2:
        if st.button("👀 Peek next", use_container_width=True):
            nxt = sched.peek_next()
            if nxt:
                st.session_state.log.insert(0, f"👀 Next job: '{nxt[1]}' (P:{nxt[0]})")
            else:
                st.session_state.log.insert(0, "📭 Queue empty")
            st.rerun()

    if st.button("🗑️ Clear all jobs", use_container_width=True):
        st.session_state.scheduler = JobScheduler()
        st.session_state.log = ["🗑️ All jobs cleared"]
        st.rerun()

# Main area – two columns
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📋 Job queue (heap order)")
    all_jobs = sched.get_all()
    if all_jobs:
        for priority, counter, desc, added_time in all_jobs:
            st.markdown(f"""
            <div style="background:#f0f2f6; padding:0.5rem; margin:0.3rem 0; border-left:4px solid {'#ff4b4b' if priority<=2 else '#ffa500' if priority<=5 else '#00cc66'}; border-radius:4px;">
                <strong>#{counter}</strong> {desc} &nbsp;&nbsp;
                <span style="background:#333; color:white; padding:2px 8px; border-radius:12px; font-size:0.8rem;">P:{priority}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No pending jobs. Add some using the sidebar.")

    # Simple heap tree visualisation (if ≤7 jobs)
    if len(all_jobs) <= 7 and len(all_jobs) > 0:
        st.subheader("🌳 Heap as a tree (min‑heap)")
        levels = []
        i = 0
        level = 0
        while i < len(all_jobs):
            count = min(2**level, len(all_jobs) - i)
            levels.append(all_jobs[i:i+count])
            i += count
            level += 1
        for lvl, nodes in enumerate(levels):
            cols = st.columns(len(nodes))
            for col, node in zip(cols, nodes):
                col.markdown(f"""
                <div style="background:linear-gradient(135deg,#667eea,#764ba2); color:white; padding:8px; border-radius:8px; text-align:center;">
                    P:{node[0]}<br/><small>#{node[1]}</small>
                </div>
                """, unsafe_allow_html=True)

with col_right:
    st.subheader("📝 Activity log")
    for entry in st.session_state.log[:15]:
        st.text(entry)
    st.caption(f"Total pending: {sched.size()}")

st.divider()
st.caption("Every `add_job` (push) and `process_next` (pop) runs in **O(log n)** – much faster than scanning a list.")