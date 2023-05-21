import '../styles/Home.css'

import { useContext } from 'react'
import { UserContext } from '../context/UserContext'
import { DataContext } from '../context/DataContext'
import { useNavigate } from 'react-router-dom'

export default function Home() {
    const navigate = useNavigate()

    const { loggedIn } = useContext(UserContext)
    const { entries } = useContext(DataContext)

    const selectEntry = (id) => {
        navigate(`/entry/${id}`)
    }

    if (!loggedIn) {
        return (
            <div className='Home'>
                <img src='/assets/lock.png' className='home-lock' onClick={() => navigate('/')}/>
            </div>
        )
    }
    else {
        return (
            <div className='Home'>
                {entries.map(entry => (
                    <div className='home-entry' onClick={() => selectEntry(`${entry.id}`)}>
                        <h2 className='home-entry-date'> {entry.date} </h2>
                    </div>
                ))}
            </div>
        )
    }
}
