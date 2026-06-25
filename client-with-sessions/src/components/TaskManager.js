import React, { useEffect, useState } from "react";
import { Button, Error, FormField, Input, Label, Textarea } from "../styles";

function TaskManager() {
  const [tasks, setTasks] = useState([]);
  const [errors, setErrors] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [priority, setPriority] = useState("medium");

  useEffect(() => {
    fetch("/tasks?page=1&per_page=10")
      .then((r) => r.json())
      .then((data) => setTasks(data.tasks || []));
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    setErrors([]);

    fetch("/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description, priority }),
    }).then((r) => {
      if (r.ok) {
        r.json().then((task) => {
          setTasks([...tasks, task]);
          setTitle("");
          setDescription("");
          setPriority("medium");
        });
      } else {
        r.json().then((err) => setErrors(err.errors || ["Something went wrong"]));
      }
    });
  }

  function toggleComplete(task) {
    fetch(`/tasks/${task.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: !task.completed }),
    })
      .then((r) => r.json())
      .then((updatedTask) => {
        setTasks(tasks.map((t) => (t.id === updatedTask.id ? updatedTask : t)));
      });
  }

  function deleteTask(id) {
    fetch(`/tasks/${id}`, {
      method: "DELETE",
    }).then((r) => {
      if (r.ok) {
        setTasks(tasks.filter((task) => task.id !== id));
      }
    });
  }

  return (
    <section>
      <h2>Your Tasks</h2>

      <form onSubmit={handleSubmit}>
        <FormField>
          <Label htmlFor="title">Title</Label>
          <Input
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </FormField>

        <FormField>
          <Label htmlFor="description">Description</Label>
          <Textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </FormField>

        <FormField>
          <Label htmlFor="priority">Priority</Label>
          <Input
            id="priority"
            value={priority}
            onChange={(e) => setPriority(e.target.value)}
          />
        </FormField>

        <Button type="submit">Add Task</Button>
      </form>

      {errors.map((err) => (
        <Error key={err}>{err}</Error>
      ))}

      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <strong>{task.title}</strong> — {task.priority}
            <p>{task.description}</p>
            <p>{task.completed ? "Complete" : "Incomplete"}</p>
            <Button onClick={() => toggleComplete(task)}>
              Toggle Complete
            </Button>
            <Button onClick={() => deleteTask(task.id)}>Delete</Button>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default TaskManager;