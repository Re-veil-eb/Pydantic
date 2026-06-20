import pytest
from models import Session, ConferenceSchedule, ProjectTimeline, HospitalShift, ShiftSchedule
from datetime import datetime

class TestConferenceSchedule:
    def test_valid_schedule(self):
        s1 = Session(start_time=datetime(2026,6,20,10), end_time=datetime(2026,6,20,11))
        s2 = Session(start_time=datetime(2026,6,20,12), end_time=datetime(2026,6,20,13))
        cs = ConferenceSchedule(sessions=[s1, s2])
        assert len(cs.sessions) == 2

    def test_invalid_schedule_overlap(self):
        s1 = Session(start_time=datetime(2026,6,20,10), end_time=datetime(2026,6,20,12))
        s2 = Session(start_time=datetime(2026,6,20,11), end_time=datetime(2026,6,20,13))
        with pytest.raises(ValueError):
            ConferenceSchedule(sessions=[s1, s2])

class TestProjectTimeline:
    def test_valid_tasks(self):
        t1 = Session(start_time=datetime(2026,6,20,10), end_time=datetime(2026,6,20,11))
        t2 = Session(start_time=datetime(2026,6,20,12), end_time=datetime(2026,6,20,13))
        pt = ProjectTimeline(project_start=datetime(2026,6,20,9), project_end=datetime(2026,6,20,14), tasks=[t1, t2])
        assert len(pt.tasks) == 2

    def test_invalid_task_outside_timeline(self):
        t1 = Session(start_time=datetime(2026,6,20,8), end_time=datetime(2026,6,20,9))
        with pytest.raises(ValueError):
            ProjectTimeline(project_start=datetime(2026,6,20,9), project_end=datetime(2026,6,20,14), tasks=[t1])

class TestShiftSchedule:
    def test_valid_shifts(self):
        s1 = HospitalShift(doctor="Dr. A", start_time=datetime(2026,6,20,10), end_time=datetime(2026,6,20,11))
        s2 = HospitalShift(doctor="Dr. A", start_time=datetime(2026,6,20,12), end_time=datetime(2026,6,20,13))
        ss = ShiftSchedule(shifts=[s1, s2])
        assert len(ss.shifts) == 2

    def test_invalid_overlapping_shifts(self):
        s1 = HospitalShift(doctor="Dr. A", start_time=datetime(2026,6,20,10), end_time=datetime(2026,6,20,12))
        s2 = HospitalShift(doctor="Dr. A", start_time=datetime(2026,6,20,11), end_time=datetime(2026,6,20,13))
        with pytest.raises(ValueError):
            ShiftSchedule(shifts=[s1, s2])
