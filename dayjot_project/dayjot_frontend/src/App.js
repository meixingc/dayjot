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

    // Get Initial Data
    useEffect(() => {
        if (user) {
            const getEntries = async () => {
                const response = await Client.get(`${BASE_URL}/entries?user=${user.id}`);
                setEntries(response.data);
                console.log('entries', response.data)
            }
            getEntries()
        }
    }, [loggedIn])

    useEffect(() => {
        if (user) {
            const getWaters = async () => {
                const response = await Client.get(`${BASE_URL}/waters?entry__user=${user.id}`)
                setWaters(response.data)
                console.log('Waters', response.data)
            }
            getWaters()
        }
    }, [loggedIn])

    useEffect(() => {
        if (user) {
            const getFoods = async () => {
                const response = await Client.get(`${BASE_URL}/foods?entry__user=${user.id}`)
                setFoods(response.data)
                console.log('Foods', response.data)
            }
            getFoods()
        }
    }, [loggedIn])

    useEffect(() => {
        if (user) {
            const getExercises = async () => {
                const response = await Client.get(`${BASE_URL}/exercises?entry__user=${user.id}`)
                setExercises(response.data)
                console.log('Exercises', response.data)
            }
            getExercises()
        }
    }, [loggedIn])

    useEffect(() => {
        if (user) {
            const getSleeps = async () => {
                const response = await Client.get(`${BASE_URL}/sleeps?entry__user=${user.id}`)
                setSleeps(response.data)
                console.log('Sleeps', response.data)
            }
            getSleeps()
        }
    }, [loggedIn])

    useEffect(() => {
        if (user) {
            const getWeights = async () => {
                const response = await Client.get(`${BASE_URL}/weights?entry__user=${user.id}`)
                setWeights(response.data)
                console.log('Weights', response.data)
            }
            getWeights()
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
