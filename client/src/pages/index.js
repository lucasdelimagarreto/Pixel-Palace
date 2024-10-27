import React,{useEffect }  from "react";
import {GameSection} from '../components/GameSection';
import style from "../styles/index.module.css"

export default function HomePage() {

    useEffect(() => {

        if (!localStorage.getItem('gameCartList')) {
            localStorage.setItem('gameList', JSON.stringify([]));
        }

      }, []);

    return(
        <div>
            <main>
            <div className={style.centerSection}><GameSection titleSection={"Jogos novos"} subTitleSection={"Jogos recém adicionados!"} isAlternateApi={false}/></div>
            <div className={style.centerSection}><GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"} isAlternateApi={false}/></div>
            <div className={style.centerSection}><GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"} isAlternateApi={false}/></div>
            <div className={style.centerSection}><GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"} isAlternateApi={false}/></div>
            <div className={style.centerSection}><GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"} isAlternateApi={false}/></div>
            </main>
        </div>
    )
}