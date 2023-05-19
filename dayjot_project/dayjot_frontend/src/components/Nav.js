import '../styles/Nav.css'
import { UserContext } from '../context/UserContext'
import { useContext } from 'react'
import { useNavigate, Link } from 'react-router-dom'

export default function Nav() {
    const navigate = useNavigate()
    const { loggedIn, handleLogOut } = useContext(UserContext)

    if (loggedIn) {
        return (
            <div className='Nav'>
                <img className='nav-logo' src='/assets/full-trans-right-invert.png'/>
                <div className='nav-right'>
                    <button className='nav-login' onClick={() => navigate('/login')}> Log In </button>
                </div>
            </div>
        )
    } 
    else {
        return (
            <div className='Nav'>
                <img className='nav-logo' src='/assets/full-trans-right-invert.png'/>
                <div className='nav-right'>
                    <Link to ='/create' className='nav-item'> Create </Link>
                    <Link to ='/entries' className='nav-item'> Entries </Link>
                    <Link to ='/profile' className='nav-item'> Profile </Link>
                    <Link to ='/' onClick={() => handleLogOut()} className='nav-item'> Log Out </Link>
                </div>
            </div>
        )
    }
}