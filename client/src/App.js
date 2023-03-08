import React, { useState, useEffect } from 'react'

function App() {
  const [data, setData] = useState([{}])
  const [data2, setData2] = useState([{}])
  const [transcript, setTranscript] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
      ).then(
        data => {
          setData(data)
          console.log(data)
        }
      )
  }, [])

  useEffect(() => {
    fetch("/members2").then(
      res2 => res2.json()
      ).then(
        data2 => {
          setData2(data2)
        }
      )
  }, [])

  useEffect(() => {
    fetch("/transcript").then(
      result => result
      ).then(
        output => {
          setTranscript(output)
          console.log(output)
        }
      )
  }, [transcript])

  return (
    <div>
      {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}
      {(typeof transcript.getTranscript === 'undefined') ? (
        <p>Loading transcript...</p>
      ) : (
        transcript.getTranscript.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}
    </div>
  )
}

export default App