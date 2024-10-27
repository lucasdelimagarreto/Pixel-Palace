import axios from 'axios';
import React,{ useState, useEffect }  from "react";
import Image from 'next/image';
import { Icon } from '@iconify/react';
import style from './styleCard.module.css'
import { useRouter } from 'next/router';

export function GameCard ({ isAlternateApi }) {
    
    const [listGames, setListGames] = useState([]);
    const router = useRouter()
    
    useEffect(() => {

        CheckGames(isAlternateApi);
        
    }, [isAlternateApi]);

      const CheckGames = (isAlternateApi) => {

        const url = isAlternateApi 
        ? `http://127.0.0.1:5123/games/alternate` 
        : `http://127.0.0.1:5123/games/all`;

        const config = isAlternateApi 
        ? { headers: { 'Authorization': `Bearer seu_token_aqui` } }
        : {};

        
        axios.get(url, config)
        .then(response => {
            
            setListGames(response.data.parameter)

         })
      .catch(error => {

        

      });

        
      

    }

    return (
        <ul className={style.gamesection}>
            {listGames && listGames.slice(0, 5).map(game => (
                <li className={style.gamesectionlist} key={game.id}>
                    <Image className={style.gameimg} src={game.imageBanner} width={220} height={110} alt="Imagem gamecard" />
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

                    <a>
                        <button className={style.buttongamecard} onClick={() => {router.push(`../../GamePageContent?gameId=${game.id}`)}}>
                        R$ {game.price}
                        </button>
                    </a>
                </li>
            ))}
        </ul>
    );
}