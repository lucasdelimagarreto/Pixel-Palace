import React,{ useState, useEffect}  from "react";
import axios from 'axios';
import { useRouter } from 'next/router';
import style from "./profileConfiguration.module.css"
import bntStyle from "../../styles/buttons.module.css"

export default function ProfileConfiguration() {
    const [user, setUser] = useState();
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [oldPassword, setOldPassword] = useState('');
    const [bornDate, setBornDate] = useState('');
    const [accessToken, setAccessToken] = useState('');
    const [message, setMessage] = useState('');

    const router = useRouter();

    useEffect(() => {
        
        const loggedInUser = localStorage.getItem("user");

        if (loggedInUser) {

          const foundUser = JSON.parse(loggedInUser);

          setUser(foundUser)
          setUsername(foundUser.username)
          setEmail(foundUser.email)
          setAccessToken(foundUser.token)
          setBornDate(foundUser.bornDate)
        }
      }, []);

    const handleLogout = () => {

        localStorage.clear();
        router.push('/register').then(() => {
            window.location.reload();
          });
      };

    const UserEdit = () => {
        const edits = [];

        if (username !== user.username) {
          edits.push({ username: username });

        }
        
        if (password !== '') {
          edits.push({ password: password });

        }
        
        if (bornDate !== user.bornDate) {
          edits.push({ age: bornDate });

        }
        
        if (email !== user.email) {
          edits.push({ email: email });

      }
      console.log(edits)

      edits.forEach(edit => UserEditApi(edit));

    }

    const UserEditApi = (userDataJson) => {

        axios.patch('http://127.0.0.1:5123/users/useredit', userDataJson, {
            headers: {
              'Authorization': `Bearer ${accessToken}`
            }
          })
            .then(() => {

                localStorage.clear();

                const loginData = {
                  email: email,
                  password: password === '' ? oldPassword : password,
              };
              
              UserLogin(loginData);      
      
            })
            .catch((error) => {
              if ((error.response && error.response.status === 409)) {
      
                setMessage(error.response.data.error_message)
      
              } else {
      
                setMessage('Erro ao enviar os dados, tente novamente dentro de alguns minutos');
      
              }
            });
    }

    const UserLogin = (userDataJson) => {

        axios.post('http://127.0.0.1:5123/users/login', userDataJson)
          .then((response) => {

            const userData = {
              username: response.data.user.username,
              email: response.data.user.email,
              bornDate: response.data.user.age,
              token: response.data.access_token,
            };

            localStorage.setItem('user', JSON.stringify(userData))

            router.push('/').then(() => {
                window.location.reload();
              });
    
          })
          .catch((error) => {
            if ((error.response && error.response.status === 409)) {
    
              setMessage(error.response.data.error_message)
    
            } else {
    
              setMessage('Erro ao enviar os dados, tente novamente dentro de alguns minutos');
    
            }
          });
    
      }


    return (
        <section className={style.sectionConfig}>
                    <div id={style.divInfos}>
                        <h1>Minha conta</h1>
                        <div className={style.logoutSection}>
                            <p>Dados de perfil</p>
                            <button className={bntStyle.bntGreenNoBorder2} onClick={handleLogout}>Fazer Logout</button>
                        </div>
                        <input type="text" placeholder="Nome de usuário" className={style.inputInfos} name="userNameRegister" 
                        value={username} onChange={(e) => setUsername(e.target.value)} />
                        <input type="email" placeholder="E-mail" className={style.inputInfos} name="emailRegister" 
                        value={email} onChange={(e) => setEmail(e.target.value)} />
                        <input type="password" placeholder="Nova senha" className={style.inputInfos} name="passwordRegister" 
                        value={password} onChange={(e) => setPassword(e.target.value)}/>
                        <input type="password" placeholder="Senha antiga" className={style.inputInfos} name="password" 
                        value={oldPassword} onChange={(e) => setOldPassword(e.target.value)}required/>
                        <div className={style.divDate}>
                            <strong>Data de Nascimento</strong>
                            <input type="date" id={style.inputDateInfos} name="dateRegister" 
                        value={bornDate} onChange={(e) => setBornDate(e.target.value)}/>
                        </div> 
                        <button className={bntStyle.bntGreenNoBorder} type='submit' name="bntConfirmConfig" onClick={UserEdit}>Salvar Alterações</button>
                        { message && <p>{message}</p>}
                    </div>
        </section>

        
    )
}