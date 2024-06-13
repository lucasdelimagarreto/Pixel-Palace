import GameOfer from "../assets/jogoOferta.png"
import Image from "next/image";
import style from "../styles/components/gamesSections.module.css"
import bntStyle from "../styles/components/buttons.module.css"
import { GameCard } from "./GameCard"

export function GameSection ({titleSection,subTitleSection}) {
    return (<section className={style.sectionJogos}>
        <div className={style.divNomeSectionJogos}>
            <h1>{titleSection}</h1>
            <button className={`${bntStyle.bntGreenNoBorder} ${style.bntSeeMore}`}>Ver Mais</button>
            <p className={style.pSubTitleDivNomeSectionJogos}>{subTitleSection}</p>
        </div>
        <div className={style.divJogosSectionjogos}>
            <GameCard/>
        </div>
    </section>)
};