import React,{ useState}  from "react";
import imgLogo from "../assets/logoPixelPalace.png"
import imgBntSearch from "../assets/bntBusca.png"
import imgWorld from "../assets/bntLinguagem.png"
import imgShop from "../assets/bntCarrinhoCompras.png"
import Image from "next/image";
import style from "../styles/header.module.css"
import bntStyle from "../styles/components/buttons.module.css"
import Register from "../pages/register";
import Link from "next/link";
import { Icon } from '@iconify/react';
import { useRouter } from 'next/router';


export default function Header () {
    const [search, setSearch] = useState('');
    const router = useRouter()
return(    <div>
        <header>
            <div>
                <a href="/">
                    <Image src={imgLogo} className={style.logoPixelPalace_header} width={200}/>
                </a>
            </div>
            <div className={style.divInputBuscaNav}>
                <div className={style.divSearchBar}>
                    <input value={search} onChange={(e) => setSearch(e.target.value)} type="text" className={style.inputSearchBar} name="searchBar" placeholder="JOGOS DE PC, MAC E CONSOLES"/>
                    <button className={style.imgBntSearch} onClick={() => {router.push(`/search?searchImput=${search}`)}}>
                        <Icon icon="ph:magnifying-glass"  style={{color: '#100f0f', fontSize: '2rem', marginRight: '0.2rem'}} />
                    </button>
                </div>
                <nav>
                    <a className={style.aNav} href="/">TODOS OS JOGOS</a>
                    <a className={style.aNav} href="/">OFERTAS QUENTES</a>
                    <a className={style.aNav} href="/">MAIS ESPERADOS</a>
                    <a className={style.aNav} href="/">NOVO</a>
                    <a className={style.aNav} href="/">XP</a>
                    <a className={style.aNav} href="/">CATEGORIAS</a>
                </nav>
            </div>
            <div className={style.divBotoesNavSuperiores}>
                <a href="/register">
                    <button className={bntStyle.bntGreenNoBorder}>ENTRAR</button>
                </a>
                <a href="">
                    <Image src={imgWorld} className={style.imgBntLinguagem} height={32} width={32}/>
                </a>
                <p className={style.pLinguagem}>PT</p>
                <a href="">
                    <Image src={imgShop} alt="" className={style.imgBntCarrinho} height={32} width={32}/>
                </a>
            </div>
        </header>
        
    </div>)
};