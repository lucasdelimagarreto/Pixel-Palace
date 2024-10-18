import { useRouter } from 'next/router';
import axios from 'axios';
import React,{ useState, useEffect }  from "react";
import { Icon } from '@iconify/react';
import Image from "next/image";
import styles from '../styles/search.module.css'



export default function Search (){
    const router = useRouter();
    const { searchImput } = router.query
    const [listGames, setListGames] = useState([]);
    
    useEffect(() => {

        CheckGames()

      }, []);

      const CheckGames = () => {
            axios.get(`http://192.168.0.8:5123/games/search?search_term=${searchImput}`)
        .then(response => {
            
            setListGames(response.data.games)

         })
      .catch(error => {

        

      });
      

    }
    return(
            <main>
               <section className={styles.sectionJogos}>
        <div className={styles.divNomeSectionJogos}>
            <h1 className={styles.titleSectionJogosSearch}>Catálogo</h1>
            <p className={styles.pSubTitleDivNomeSectionJogos}><strong>Você pesquisou por: </strong>{searchImput} </p>
        </div>
        <div className={styles.divJogosSectionjogos}>
        <ul className={styles.gamesection}>
            {listGames && listGames.map(game => (
                <li className={styles.gamesectionlist} key={game.id}>
                    <Image className={styles.gameimg} src={game.imageBanner} width={220} height={110} alt="Imagem gamecard" />
                    <p className={styles.titlegamecard}>
                        {game.gameName} {game.secondGameName && game.secondGameName }
                    </p>
                    
                        {game.plataform == "Steam"? (
                        <div className={styles.iconsection}>
                            <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                            <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                        </div>)
                    : (
                        <div className={styles.iconsection}>
                            <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                        </div>
                    )}

                    <a>
                        <button className={styles.buttongamecard} onClick={() => {router.push(`/gamePageContent?gameId=${game.id}`)}}>
                        R$ {game.price}
                        </button>
                    </a>
                </li>
            ))}
        </ul>
        </div>
    </section>
               

            </main>
    )
}