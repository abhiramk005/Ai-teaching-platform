import { Routes, Route } from "react-router-dom";
import WelcomePage from "./pages/WelcomePage";
import HomePage from "./pages/Home";
import Login from "./pages/Login"
import Signup from "./pages/Signup";
import ProtectedRoute from "./components/ProtectedRoute";



function App() {
  return (
    <Routes>
      <Route path="/" element={<WelcomePage />} />
      <Route path="/login" element={<Login/>}/>
      <Route path="/signup" element={<Signup/>}/>
      <Route 
        path="/home" 
          element={<ProtectedRoute>
              <HomePage />
            </ProtectedRoute>} />
    </Routes>
  );
}

export default App;
