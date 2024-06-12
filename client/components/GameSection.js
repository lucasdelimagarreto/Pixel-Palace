import GameOfer from "../assets/jogoOferta.png"
import Image from "next/image";
import style from "../styles/components/gamesSections.module.css"
import bntStyle from "../styles/components/buttons.module.css"
import GameCard from "./GameCard"

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

export function GameSectionSearch ({searchImput}) {
    return (<section className={style.sectionJogos}>
        <div className={style.divNomeSectionJogos}>
            <h1 className={style.titleSectionJogosSearch}>Catálogo</h1>
            <p className={style.pSubTitleDivNomeSectionJogos}><strong>Você pesquisou por: </strong>{searchImput} </p>
        </div>
        <div className={style.divJogosSectionjogos}>
            <GameCard/>
        </div>
    </section>)
}