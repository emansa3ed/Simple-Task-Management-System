from project import TaskMaster

def test_create(monkeypatch):
    task_master = TaskMaster()
    monkeypatch.setattr("builtins.input", lambda _: "wash the dishes")
    task_master.create()
    assert task_master.database == [{"ID": 1, "Task": "wash the dishes", "Done": False}] and task_master.count == 1

def test_update(monkeypatch):
    task_master = TaskMaster()
    task_master.database = [{"ID": 1, "Task": "wash the dishes", "Done": False}]
    inputs = iter(["1", "do the laundry"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    task_master.update()
    assert task_master.database == [{"ID": 1, "Task": "do the laundry", "Done": False}]

def test_delete(monkeypatch):
    task_master = TaskMaster()
    task_master.database = [{"ID": 1, "Task": "do the laundry", "Done": False}]
    monkeypatch.setattr("builtins.input", lambda _: "1")
    task_master.delete()
    assert task_master.database == []

def test_mark_done(monkeypatch):
    task_master = TaskMaster()
    task_master.database = [{"ID": 1, "Task": "do the laundry", "Done": False}]
    inputs = iter(["1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    task_master.mark_done()
    assert task_master.database == [{"ID": 1, "Task": "do the laundry", "Done": True}]
