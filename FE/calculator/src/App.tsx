import React, {useEffect, useState} from 'react';
import {getSupportedOperators, postCalculate} from "./service/api";
import {postCalculateRequest} from "./service/requests";

function App() {
    const [operators, setSupportedOperators] = useState<string[]>([])
    const [result, setResult] = useState<number | undefined>(undefined)
    const [requestData, setRequestData] = useState<postCalculateRequest>({
        operator: undefined, operand_a: undefined, operand_b: undefined
    })

    useEffect(() => {
        getSupportedOperators().then((e) => {
            setSupportedOperators(e.operators)
        })
    }, [])

    const calculate = async () => {
        try {
            const newResult = await postCalculate(requestData)
            setResult(newResult.result)
        } catch (e) {
            console.error(e)
        }
    }
    return (
        <div className="card">
            <h2>
                Welcome to an extremely over-engineered calculator
            </h2>
            <div className="input__container">
                <label className="input">
                    <input className="input__field" type="number" placeholder=" "
                           onChange={e => setRequestData({...requestData, operand_a: e.target.valueAsNumber})}/>
                    <span className="input__label">Operand A</span>
                </label>
                <label className="input">
                    <select className="input__field"
                            onChange={e => setRequestData({...requestData, operator: e.target.value})}>
                        <option disabled selected> Please select an option</option>
                        {
                            operators.map((operator) => <option value={operator}>{operator}</option>)
                        }
                    </select>
                    <span className="input__label">Operator</span>
                </label>
                <label className="input">
                    <input className="input__field" type="number" placeholder=" "
                           onChange={e => setRequestData({...requestData, operand_b: e.target.valueAsNumber})}/>
                    <span className="input__label">Operand B</span>
                </label>
                <h2>=</h2>
                <label className="input">
                    <input className="input__field" disabled={true} value={result} type="text"/>
                </label>
            </div>
            <div className="button-group">
                <button onClick={calculate}>Calculate</button>
            </div>
            <span className="calculationResult"></span>
        </div>
    );
}

export default App;
