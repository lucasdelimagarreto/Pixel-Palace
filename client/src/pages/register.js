import style from "../styles/styleCadastro.module.css"
import bntStyle from "../styles/buttons.module.css"
import { useState } from 'react';
import axios from 'axios';
import { useRouter } from 'next/router';


export default function Register() {

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [emailLogin, setEmailLogin] = useState('');
    const [passwordLogin, setPasswordLogin] = useState('');
    const [bornDate, setBornDate] = useState('');
    const [message, setMessage] = useState('');

    const router = useRouter();

    const UserRegister = () => {

        const userDataJson = {
          username: username,
          email: email,
          password: password,
          age: bornDate
        };

        axios.post('http://127.0.0.1:5123/users', userDataJson)
          .then((response) => {
            setUsername('');
            setEmail('');
            setPassword('');
            setBornDate('');

            router.push('/');
    
          })
          .catch((error) => {
            if ((error.response && error.response.status === 409)) {
    
              setMessage(error.response.data.error_message)
    
            } else {
    
              setMessage('Erro ao enviar os dados, tente novamente dentro de alguns minutos');
    
            }
          });
    
      }    
      const UserLogin = () => {

        const userDataJson = {
          email: emailLogin,
          password: passwordLogin,
        };

        axios.post('http://127.0.0.1:5123/users/login', userDataJson)
          .then((response) => {
            setEmailLogin('');
            setPasswordLogin('');

            const userData = {
              username: response.data.user.username,
              email: response.data.user.email,
              token: response.data.access_token,
            };

            localStorage.setItem('user', JSON.stringify(userData))

            router.push('/');
    
          })
          .catch((error) => {
            if ((error.response && error.response.status === 409)) {
    
              setMessage(error.response.data.error_message)
    
            } else {
    
              setMessage('Erro ao enviar os dados, tente novamente dentro de alguns minutos');
    
            }
          });
    
      }

    return(
            <main className={style.mainRegister}>

                <div id={style.divRegisterLoginLayout}>
                    <div id={style.divLogin}>
                        <h2 className={style.h2TitleRegisterLogin}>Entrar</h2>
                        <input type="email" placeholder="E-mail" className={style.inputLogin} name="emailLogin" value={emailLogin} onChange={(e) => setEmailLogin(e.target.value)} required />
                        <input type="password" placeholder="Senha" className={style.inputLogin} name="passwordLogin" value={passwordLogin} onChange={(e) => setPasswordLogin(e.target.value)} required/>
                        <input type="checkbox" checked="checked" className={`${style.inputCheckbox} ${style.checkbox}`} name="renemberMeLogin"/> Lembrar de mim
                        <button className={bntStyle.bntGreenNoBorder2} name="bntEntrarLogin" onClick={UserLogin}>Entrar</button>
                        <a href="" id={style.aForgotPassword}>Esqueceu sua senha?</a>
                    </div>
                    <div id={style.divOrRegisterLogin}>
                        <h2 className={style.h2TitleRegisterLogin}>OU</h2>
                        <div id={style.divHorizontalLine}></div>
                    </div>
                    <div id={style.divRegister}>
                        <h2 className={style.h2TitleRegisterLogin}>Criar conta</h2>
                        <input type="text" placeholder="Nome de usuário" className={style.inputLogin} name="userNameRegister" 
                        value={username} onChange={(e) => setUsername(e.target.value)} required/>
                        <input type="email" placeholder="E-mail" className={style.inputLogin} name="emailRegister" 
                        value={email} onChange={(e) => setEmail(e.target.value)} required/>
                        <input type="password" placeholder="Senha" className={style.inputLogin} name="passwordRegister" 
                        value={password} onChange={(e) => setPassword(e.target.value)}required/>
                        <strong id={style.textDate}>Data de Nascimento</strong>
                        <input type="date" id={style.inputDateRegister} name="dateRegister" 
                        value={bornDate} onChange={(e) => setBornDate(e.target.value)} required/>
                        <br/>
                        <input type="checkbox" checked="checked" className={`${style.inputCheckbox} ${style.checkbox}`} name="aceptTerms"/>Eu aceito os <a href="">termos e condições</a>, <a href="">a política de cookies</a><br/> e <a href="">a política de privacidade</a>.
                        <button className={bntStyle.bntGreenNoBorder2} type='submit' name="bntRegistrarRegister" onClick={UserRegister}>Registrar</button>
                        { message && <p>{message}</p>}
                    </div>
                </div>
            </main>
    )
}