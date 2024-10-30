import bntStyle from "../../styles/buttons.module.css"
import axios from 'axios';
import React,{ useState, useEffect }  from "react";
import Image from 'next/image';
import { Icon } from '@iconify/react';
import style from './GamesCardProfile.module.css'
import { useRouter } from 'next/router';

export default function GameCardProfile () {
    const [listGames, setListGames] = useState([]);
    const [user, setUser] = useState();
    const router = useRouter()

    useEffect(() => {
        
        const loggedInUser = localStorage.getItem("user");

        if (loggedInUser) {

          const foundUser = JSON.parse(loggedInUser);

          setUser(foundUser)


        }
      }, []);

    useEffect(() => {
        if (user) {
            CheckGames();
        }
    }, [user]);

    

    
    const CheckGames = async () => {

        const userGamesResponse = await axios.get(`http://127.0.0.1:5123/users/user_games?user_id=${user.user_id}`);
            const idsGame = userGamesResponse.data.games;

            const allGamesResponse = await axios.get('http://127.0.0.1:5123/games/all');
            const allGames = allGamesResponse.data.parameter;

            const filteredGames = allGames.filter(game => idsGame.some(userGame => userGame.id === game.id))

            setListGames(filteredGames);

    }

    return (
        <section className={style.sectionJogos}>
        <div className={style.divNomeSectionJogos}>
            <h1>Minha conta</h1>
            <p className={style.pSubTitleDivNomeSectionJogos}>Minha lista de favoritos</p>
        </div>
        <div className={style.divJogosSectionjogos}>
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
        </div>
    </section>
    )
}