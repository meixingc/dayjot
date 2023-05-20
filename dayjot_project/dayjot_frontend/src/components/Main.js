import { Routes, Route } from 'react-router-dom'
import Home from './Home'
import Login from './user/Login'
import Register from './user/Register'
import UpdateProfile from './user/UpdateProfile'
import NewEntry from './entry/NewEntry'
import Entry from './entry/Entry'
import UpdateEntry from './entry/UpdateEntry'

export default function Main() {
    return (
        <div className='Main'>
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/login' element={<Login />} />
                <Route path='/register' element={<Register />} />
                <Route path='/profile/update' element={<UpdateProfile />} />
                <Route path='/new' element={<NewEntry />} />
                <Route path='/entry/:id' element={<Entry />} />
                <Route path='/entry/update/:id' element={<UpdateEntry />} />
            </Routes>
        </div>
    )
}