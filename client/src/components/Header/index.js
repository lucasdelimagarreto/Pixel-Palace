import React,{ useState, useEffect}  from "react";
import Link from 'next/link';
import imgLogo from "../../assets/logoPixelPalace.png"
import imgWorld from "../../assets/bntLinguagem.png"
import imgShop from "../../assets/bntCarrinhoCompras.png"
import bntStyle from "../../styles/buttons.module.css"
import { Icon } from '@iconify/react';
import { useRouter } from 'next/router';
import style from "./header.module.css"
import Image from "next/image";



export default function Header () {
    const [search, setSearch] = useState('');
    const router = useRouter()
    const [user, setUser] = useState();
    const [gameCountCart, setGameCountCart] = useState(0);

    useEffect(() => {
        
        const loggedInUser = localStorage.getItem("user");

        if (loggedInUser) {

          const foundUser = JSON.parse(loggedInUser);

          setUser(foundUser);

        }
      }, []);

      useEffect(() => {

        const interval = setInterval(() => {
          const storedGames = JSON.parse(localStorage.getItem('gameCartList')) || [];
          setGameCountCart(storedGames.length);
        }, 1000);
      
        return () => clearInterval(interval);

      }, []);
      


return(
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
        {user ?(

            <Link href="/profile" style={{ textDecoration: 'none', display: 'flex', alignItems: 'center' }}>
                <p style={{marginRight: '0.5rem'}}>{user && user.username}</p>
                <Icon icon="iconoir:profile-circle" width="2rem" height="2rem"  style={{color: '#fff'}} />
            </Link>
        ) : (
            <a href="/register">
            <button className={bntStyle.bntGreenNoBorder}>ENTRAR</button>
        </a>
        )
        }
        <a href="">
            <Image src={imgWorld} className={style.imgBntLinguagem} height={32} width={32}/>
        </a>
        <p className={style.pLinguagem}>PT</p>
        <Link href={gameCountCart > 0 ? "/Cart" : "#"} className={style.buttonCart}>
            <Image src={imgShop} alt="" className={style.imgBntCarrinho} height={32} width={32}/>
            <p>{gameCountCart}</p>
        </Link>
    </div>
</header>)
};