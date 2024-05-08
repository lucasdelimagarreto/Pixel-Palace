import GameOfer from "../assets/jogoOferta.png"
import Image from "next/image";
import style from "../styles/components/gamesSections.module.css"
import bntStyle from "../styles/components/buttons.module.css"

const GameSection = () => (
    <section className={style.sectionJogos}>
        <div className={style.divNomeSectionJogos}>
            <h1>Ofertas</h1>
            <button className={`${bntStyle.bntGreenBoldBlackBorder} ${style.bntSeeMore}`}>Ver Mais</button>
            <p className={style.pSubTitleDivNomeSectionJogos}>Jogos com até 95% de desconto!</p>
        </div>
        <div className={style.divJogosSectionjogos}>
            <Image src={GameOfer} class={style.imgJogoOferta} height={260} alt=""/>
            <Image src={GameOfer} class={style.imgJogoOferta} height={260} alt=""/>
            <Image src={GameOfer} class={style.imgJogoOferta} height={260} alt=""/>
            <Image src={GameOfer} class={style.imgJogoOferta} height={260} alt=""/>
            <Image src={GameOfer} class={style.imgJogoOferta} height={260} alt=""/>
        </div>
    </section>
);

export default GameSection;