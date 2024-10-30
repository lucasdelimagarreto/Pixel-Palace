import React,{ useState, useEffect}  from "react";
import Link from 'next/link';
import { Icon } from '@iconify/react';
import style from "../styles/profile.module.css"
import ProfileConfiguration from "@/components/ProfileConfiguration";
import PurchasedGamesCard from "@/components/PurchasedGamesCard"
import GameCardProfile from '@/components/GamesCardProfile';

export default function Profile() {
    const [user, setUser] = useState();
    const [Screen, setScreen] = useState('profileConfiguration');
    const [isBarVisible, setBarVisible] = useState(false);

    useEffect(() => {

        const loggedInUser = localStorage.getItem("user");

        if (loggedInUser) {

          const foundUser = JSON.parse(loggedInUser);

          setUser(foundUser);

        }
      }, []);

      const ControlScreen = (dataScreen) => {
        setScreen(dataScreen)
        setBarVisible(!isBarVisible);
    }

    let renderContent;

    if (Screen === 'purchasedGames') {
        renderContent = <PurchasedGamesCard />;
        
    } else if (Screen === 'wishList') {
      renderContent = <GameCardProfile/>;
      
    } else if (Screen === 'profileConfiguration') {
        renderContent = <ProfileConfiguration />;
    }

    return(
        <main>
            <div className={style.sectionProfileGeneral}>            
            <div className={style.sectionProfile}>
            <Link href="/profile" style={{ textDecoration: 'none'}}>
                <Icon icon="iconoir:profile-circle" width="10rem" height="10rem"  style={{color: '#fff'}} />
            </Link>

                <div>
                    <h1 style={{marginLeft: '1rem', fontSize: '3rem'}}>{user && user.username}</h1>
                    <div>

                        <button className={style.buttonOption} onClick={() => ControlScreen('purchasedGames')}>
                            Meus jogos adquiridos
                        </button>
                        
                        <button className={style.buttonOption} onClick={() => ControlScreen('wishList')}>
                            Minha lista de desejos
                        </button>
                        
                        <button className={style.buttonOption} onClick={() => ControlScreen('profileConfiguration')}>
                            Dados do perfil
                        </button>
                    
                    </div>
                </div>
            </div>
            </div>

            {renderContent}
        </main>
    )
}