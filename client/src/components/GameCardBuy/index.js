import React,{ useState, useEffect}  from "react";
import style from "./gameCardBuy.module.css";
import Image from 'next/image';
import { Icon } from '@iconify/react';
import { useRouter } from 'next/router';


export function GameCardBuy () {

    const router = useRouter()
    const [cartList, setCartList] = useState();

    useEffect(() => {

        const storedGameCartList = localStorage.getItem('gameCartList');

        if (storedGameCartList) {

          const foundStoredGameCartList = JSON.parse(storedGameCartList);

          setCartList(foundStoredGameCartList);


        }
      }, []);

      const deleteGameFromLocalStorage = (gameId) => {
        const storedGames = JSON.parse(localStorage.getItem('gameCartList')) || [];
        
        const updatedGames = storedGames.filter(game => game.id !== gameId);
    
        localStorage.setItem('gameCartList', JSON.stringify(updatedGames));

        setCartList(updatedGames)
      };
      
      


    return (
        <>
        {cartList && cartList.map(game => (
        <div className={style.cardSection}>
            <Image className={style.gameimg} src={game.imageBanner} width={210} height={100} alt="Imagem gamecard" />
            <div>
                <div>
                    <p className={style.titlegamecard}>
                        {game.gameName} {game.secondGameName && game.secondGameName }
                    </p>
                    
                        {game.platform == "Steam"? (
                        <div className={style.iconsection}>
                            <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                            <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                        </div>)
                    : (
                        <div className={style.iconsection}>
                            <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                        </div>
                    )}
                </div>

                <div className={style.buyGameCard}>
                    <a>
                        <button className={style.buttongamecard} onClick={() => {router.push(`../../GamePageContent?gameId=${game.id}`)}}>
                        R$ {game.price}
                        </button>
                    </a>

                    <button className={style.trashButton} onClick={() => deleteGameFromLocalStorage(game.id)}>
                        <Icon icon="jam:trash-f" width="2rem" height="2rem"  style={{color: '#96A6B7'}} />
                    </button>

                </div>
            </div>
        </div>))}</>
    )
}