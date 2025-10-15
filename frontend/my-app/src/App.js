import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./components/Login";
import Register from "./components/Register";
import Homepage from "./components/Homepage";
import Navbar from "./components/Navbar";
import TaskPage from "./components/TaskPage";
import "./styles.css"; // Import the styles.css file
function App() {
  return (
    <Router>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/taskpage" element={<TaskPage />} />
        </Routes>
      </div>
    </Router>
  );
}
export default App;
