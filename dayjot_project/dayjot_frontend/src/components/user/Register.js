import '../../styles/Register.css'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { RegisterUser } from '../../services/Auth'

export default function Register() {
    const navigate = useNavigate()

    const [ formValues, setFormValues ] = useState({
        picture: '',
        name: '',
        username: '',
        email: '',
        password: ''
    })

    const handleChange = (e) => {
        setFormValues({...formValues, [e.target.name]: e.target.value})
    }

    const handleSubmit = async(e) => {
        e.preventDefault()
        await RegisterUser({
            picture: formValues.picture,
            first_name: formValues.name,
            username: formValues.username,
            email: formValues.email,
            password: formValues.password
        })
        setFormValues({
            picture: '',
            name: '',
            username: '',
            email: '',
            password: ''
        })
        navigate('/login')
    }

    return (
        <div className='Register'>
            <form onSubmit={handleSubmit} className='registerform'>
                <div className='registerinput'>
                    <label className='registerlabel'> Picture: </label>
                    <input type='text' name='picture' value={formValues.picture} onChange={handleChange} />
                </div>
                <div className='registerinput'>
                    <label className='registerlabel'> Name: </label>
                    <input type='text' name='name' value={formValues.name} onChange={handleChange} />
                </div>
                <div className='registerinput'>
                    <label className='registerlabel'> Username: </label>
                    <input type='text' name='username' value={formValues.username} onChange={handleChange} />
                </div>
                <div className='registerinput'>
                    <label className='registerlabel'> Email: </label>
                    <input type='email' name='email' value={formValues.email} onChange={handleChange} />
                </div>
                <div className='registerinput'>
                    <label className='registerlabel'> Password: </label>
                    <input type='password' name='password' value={formValues.password} onChange={handleChange} />
                </div>
                <button type='submit' className='register'> Register </button>
            </form>
        </div>
    )
}