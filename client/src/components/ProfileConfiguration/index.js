import React,{ useState, useEffect}  from "react";
import { useRouter } from 'next/router';
import style from "./profileConfiguration.module.css"
import bntStyle from "../../styles/buttons.module.css"

export default function ProfileConfiguration() {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('')
    const [bornDate, setBornDate] = useState('');
    const [message, setMessage] = useState('');

    const router = useRouter();

    const handleLogout = () => {

        localStorage.clear();
        router.push('/register');
      
      };

    return (
        <section className={style.sectionConfig}>
                    <div id={style.divInfos}>
                        <h1>Minha conta</h1>
                        <div className={style.logoutSection}>
                            <p>Dados de perfil</p>
                            <button className={bntStyle.bntGreenNoBorder2} onClick={handleLogout}>Fazer Logout</button>
                        </div>
                        <input type="text" placeholder="Nome de usuário" className={style.inputInfos} name="userNameRegister" 
                        value={username} onChange={(e) => setUsername(e.target.value)} required/>
                        <input type="email" placeholder="E-mail" className={style.inputInfos} name="emailRegister" 
                        value={email} onChange={(e) => setEmail(e.target.value)} required/>
                        <input type="password" placeholder="Senha" className={style.inputInfos} name="passwordRegister" 
                        value={password} onChange={(e) => setPassword(e.target.value)}required/>
                        <div className={style.divDate}>
                            <strong>Data de Nascimento</strong>
                            <input type="date" id={style.inputDateInfos} name="dateRegister" 
                        value={bornDate} onChange={(e) => setBornDate(e.target.value)} required/>
                        </div> 
                        <button className={bntStyle.bntGreenNoBorder} type='submit' name="bntConfirmConfig">Salvar Alterações</button>
                        { message && <p>{message}</p>}
                    </div>
        </section>

        
    )
}