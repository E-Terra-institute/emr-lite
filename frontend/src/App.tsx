import { useEffect, useState } from 'react'
import axios from 'axios'

interface Patient {
  id: number
  full_name: string
  date_of_birth: string
  phone: string
  address?: string
}

function App() {
  const [patients, setPatients] = useState<Patient[]>([])

  useEffect(() => {
    axios.get('/patients').then(res => setPatients(res.data))
  }, [])

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Пациенты</h1>
      <ul>
        {patients.map(p => (
          <li key={p.id}>
            {p.full_name} — {p.date_of_birth}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App

