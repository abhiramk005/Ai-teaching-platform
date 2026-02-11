import { useState, useContext } from "react";
import { AuthContext } from "../context/authContext";
import { useNavigate, Link } from "react-router-dom";

function Login() {
  const { login } = useContext(AuthContext);
  const navigate = useNavigate();

  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  const [error, setError] = useState("");


  const handleChange = (e) =>{
    setForm({ ...form, [e.target.name]: e.target.value });
    setError(""); 
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        await login(form);
        navigate("/home");
    } catch (err) {
        setError(err.response?.data?.error || "Login failed");
    }
  };

  return (
    <div className="login-div">
      <form onSubmit={handleSubmit}>
        <input
          name="email"
          placeholder="Email"
          onChange={handleChange}
        />
        <br /><br />

        <input
          name="password"
          type="password"
          placeholder="Password"
          onChange={handleChange}
        />
        <br /><br />

        <button type="submit">Login</button>
      </form>

      {error && (
        <p style={{ color: "red", marginTop: "10px" }}>
        {error}
        </p>
        )}

      {/* New user navigation */}
      <p style={{ marginTop: "20px" }}>
        New user?{" "}
        <Link to="/signup" style={{ color: "#2563eb", fontWeight: "500" }}>
          Create an account
        </Link>
      </p>
      
    </div>

  );
}

export default Login;
