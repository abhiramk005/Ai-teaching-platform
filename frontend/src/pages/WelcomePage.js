import {useNavigate} from 'react-router-dom'

const WelcomePage = () => {
    const navigate=useNavigate()
    return (
        <div className="welcome">
            <div className="welcome-contents">
                <h1>Welcome to Ai powered teacher</h1>
                <p>upload images or pdf to learn interactievly </p>
                <button className='go-button' onClick={()=>{navigate("/login")}}>LET'S GO</button>
            </div>
            
        </div>
        
    );
}
 
export default WelcomePage;