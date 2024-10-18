import React from "react"
import {GameSection} from '../components/GameSection';

export default function HomePage() {
    return(
        <div>
            <main>
                <GameSection titleSection={"Jogos novos"} subTitleSection={"Jogos recém adicionados!"}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"}/>
            </main>
        </div>
    )
}