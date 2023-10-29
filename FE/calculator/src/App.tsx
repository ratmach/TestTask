import React, {useEffect, useState} from 'react';
import './App.css';
import {getSupportedOperators} from "./service/api";

function App() {
    const [operators, setSupportedOperators] = useState<string[]>([]);
    useEffect(() => {
        getSupportedOperators().then((e) => {
            setSupportedOperators(e.operators)
        })
    }, [])
    return (
        <div className="calculator">
            <input type="number"/>
            <select>
                {
                    operators.map((operator) => <option value="{operator}">{operator}</option>)
                }
            </select>
            <input type="number"/>
        </div>
    );
}

export default App;
