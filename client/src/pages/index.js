import React,{useEffect }  from "react";
import {GameSection} from '../components/GameSection';

export default function HomePage() {

    useEffect(() => {

        if (!localStorage.getItem('gameCartList')) {
            localStorage.setItem('gameList', JSON.stringify([]));
        }

      }, []);

    return(
        <div>
            <main>
                <GameSection titleSection={"Jogos novos"} subTitleSection={"Jogos recém adicionados!"} isAlternateApi={false}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"} isAlternateApi={false}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"} isAlternateApi={false}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"} isAlternateApi={false}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"} isAlternateApi={false}/>
            </main>
        </div>
    )
}