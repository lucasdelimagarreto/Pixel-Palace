import imgLogo from "../assets/logoPixelPalace.png"
import imgBntSearch from "../assets/bntBusca.png"
import imgWorld from "../assets/bntLinguagem.png"
import imgShop from "../assets/bntCarrinhoCompras.png"
import Image from "next/image";
import style from "../styles/header.module.css"
import bntStyle from "../styles/components/buttons.module.css"
import Register from "../pages/register";
import Link from "next/link";

const Header = () => (
    <div>
        <header>
            <div>
                <a href="/">
                    <Image src={imgLogo} className={style.logoPixelPalace_header} width={200}/>
                </a>
            </div>
            <div className={style.divInputBuscaNav}>
                <div className={style.divSearchBar}>
                    <input type="text" className={style.inputSearchBar} name="searchBar" placeholder="JOGOS DE PC, MAC E CONSOLES"/>
                    <Image src={imgBntSearch} alt="" width={43} height={43}/>
                </div>
                <nav>
                    <a className="aNav" href="/">TODOS OS JOGOS</a>
                    <a className="aNav" href="/">OFERTAS QUENTES</a>
                    <a className="aNav" href="/">MAIS ESPERADOS</a>
                    <a className="aNav" href="/">NOVO</a>
                    <a className="aNav" href="/">XP</a>
                    <a className="aNav" href="/">COMUNIDADE</a>
                </nav>
            </div>
            <div className="divBotoesNavSuperiores">
                <a href="/register">
                    <button className={bntStyle.bntGreenNoBorder}>ENTRAR</button>
                </a>
                <a href="">
                    <Image src={imgWorld} className="imgBntLinguagem" height={32} width={32}/>
                </a>
                <p className="pLinguagem">PT</p>
                <a href="">
                    <Image src={imgShop} alt="" className="imgBntCarrinho" height={32} width={32}/>
                </a>
            </div>
        </header>
        
    </div>
);

export default Header;