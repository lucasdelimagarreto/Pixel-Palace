import bntStyle from "../../styles/buttons.module.css"
import style from "./gamesSections.module.css"
import { GameCard } from "../GameCard"

export function GameSection ({titleSection,subTitleSection, isAlternateApi}) {
    return (
        <section className={style.sectionJogos}>
        <div className={style.divNomeSectionJogos}>
            <h1>{titleSection}</h1>
            {isAlternateApi? <></> : <button className={`${bntStyle.bntGreenNoBorder} ${style.bntSeeMore}`}>Ver Mais</button>}
            <p className={style.pSubTitleDivNomeSectionJogos}>{subTitleSection}</p>
        </div>
        <div className={style.divJogosSectionjogos}>
            <GameCard isAlternateApi={isAlternateApi}/>
        </div>
    </section>)
};