import './App.css'
import { useState, useEffect } from 'react'
import { UserContext } from './context/UserContext'
import { DataContext } from './context/DataContext'
import { CheckSession } from './services/Auth'
import { BASE_URL } from './services/api'
import Client from './services/api'

import Nav from './components/Nav'
import Main from './components/Main'

export default function App() {
    // States
    const [ loggedIn, setLoggedIn ] = useState(localStorage.getItem("loggedIn") == "true")
    const [ user, setUser ] = useState(null)
    const [ entries, setEntries ] = useState([])
    const [ waters, setWaters ] = useState([])
    const [ foods, setFoods ] = useState([])
    const [ exercises, setExercises ] = useState([])
    const [ sleeps, setSleeps ] = useState([])
    const [ weights, setWeights ] = useState([])

    // Auth
    const handleLogOut = () => {
        localStorage.removeItem('jwt')
        setLoggedIn(false)
        setUser(null)
    }

    useEffect(() => {
        const getSession = async () => {
            const sessionUser = await CheckSession()
            setUser(sessionUser)
            setLoggedIn(sessionUser !== null)
        }
        getSession()
    }, [])

    useEffect(() => {
        if (user) {
            console.log(user)
        }
        else {
            console.log('No user data')
        }
    }, [user])

    // Get Initial Data
    useEffect(() => {
        if (user) {
            const getEntries = async () => {
                const response = await Client.get(`${BASE_URL}/entries`)
                const results = await response.data.filter(entry => entry.user === user.id)
                setEntries(results)
                console.log('Entries', results)
            }
            getEntries()
        }
    }, [loggedIn])

    useEffect(() => {
        if (user && entries) {
            const getWaters = async () => {
                const response = await Client.get(`${BASE_URL}/waters`)
                const results = await response.data.filter(water => entries.some(entry => entry.id === water.entry && entry.user === user.id)) 
                setWaters(results)
                console.log('Waters', results) 
            }
            getWaters()
        }
    }, [loggedIn])

    useEffect(() => {
        if (user && entries) {
            const getFoods = async () => {
                const response = await Client.get(`${BASE_URL}/foods`)
                const results = await response.data.filter(food => entries.some(entry => entry.id === food.entry && entry.user === user.id)) 
                setFoods(results)
                console.log('Foods', results) 
            }
            getFoods()
        }
    }, [loggedIn])

    useEffect(() => {
        if (user && entries) {
            const getExercises = async () => {
                const response = await Client.get(`${BASE_URL}/exercises`)
                const results = await response.data.filter(exercise => entries.some(entry => entry.id === exercise.entry && entry.user === user.id)) 
                setExercises(results)
                console.log('Exercises', results) 
            }
            getExercises()
        }
    }, [loggedIn])

    return (
        <div className='App'>
            <UserContext.Provider value={{ user, setUser, loggedIn, setLoggedIn, handleLogOut }}>
                <Nav />
                <DataContext.Provider value={{ entries, waters, foods, exercises, sleeps, weights}}>
                    <Main />
                </DataContext.Provider>
            </UserContext.Provider>
        </div>
    )
}
