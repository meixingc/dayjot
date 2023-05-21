import '../../styles/Entry.css'

import { useContext } from 'react'
import { DataContext } from '../../context/DataContext'
import { useNavigate } from 'react-router-dom'
import { useParams } from 'react-router-dom'

export default function Entry() {
    const navigate = useNavigate()

    const { id } = useParams()
    const { entries, waters, foods, exercises } = useContext(DataContext)

    const entry = entries.find(entry => entry.id == id)
    const water = waters.filter(water => water.entry == id)
    const food = foods.filter(food => food.entry == id)
    const exercise = exercises.filter(exercise => exercise.entry == id)

    if (entry) {
        return (
            <div className='Entry'>
                <h1 className='entry-date'> {entry.date} </h1>
                <div>
                    <h1> Waters </h1>
                    {
                        water.map(water => (
                            <div>
                                <h2> {water.amount} ml </h2>
                            </div>
                        ))
                    }
                </div>
                <div>
                    <h1> Foods </h1>
                    {
                        food.map(food => (
                            <div>
                                <h2> {food.name} </h2>
                                <h2> {food.calories} calories </h2>
                            </div>
                        ))
                    }
                </div>
                <div>
                    <h1> Exercises </h1>
                    {
                        exercise.map(exercise => (
                            <div>
                                <h2> {exercise.name} </h2>
                                <h2> {exercise.calories} calories </h2>
                            </div>
                        ))
                    }
                </div>
                <button className='entry-edit' onClick={() => navigate(`/entry/edit/${id}`)}> Edit Entry </button>
            </div>
        )
    }
}