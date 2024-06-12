import Image from 'next/image';
import { Icon } from '@iconify/react';
import style from './styleCard.module.css'

export default function GameCard () {
    return (
        <ul className={style.gamesection}>
            <li className={style.gamesectionlist}>
                <Image className={style.gameimg} src="https://assets.nuuvem.com/image/upload/t_product_sharing_banner/v1/products/557dbb9f69702d0a9c7da700/sharing_images/nok69j6m12kgovgokrbh.jpg" width={220} height={110} alt="Imagem gamecard" />
                <p className={style.titlegamecard}>
                    Batman Arkham
                </p>
                <div className={style.iconsection}>
                    <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                    <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                </div>

                <a href="/gamePageContent">
                    <button className={style.buttongamecard}>
                    R$ 41,99
                    </button>
                </a>
            </li>

            <li className={style.gamesectionlist}>
                <Image className={style.gameimg} src="https://assets.nuuvem.com/image/upload/t_product_sharing_banner/v1/products/557dbb9f69702d0a9c7da700/sharing_images/nok69j6m12kgovgokrbh.jpg" width={220} height={110} alt="Imagem gamecard" />
                <p className={style.titlegamecard}>
                    Batman Arkham
                </p>
                <div className={style.iconsection}>
                    <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                    <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                </div>

                <a href="/gamePageContent">
                    <button className={style.buttongamecard}>
                    R$ 41,99
                    </button>
                </a>
            </li>

            <li className={style.gamesectionlist}>
                <Image className={style.gameimg} src="https://assets.nuuvem.com/image/upload/t_product_sharing_banner/v1/products/557dbb9f69702d0a9c7da700/sharing_images/nok69j6m12kgovgokrbh.jpg" width={220} height={110} alt="Imagem gamecard" />
                <p className={style.titlegamecard}>
                    Batman Arkham
                </p>
                <div className={style.iconsection}>
                    <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                    <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                </div>

                <a href="/gamePageContent">
                    <button className={style.buttongamecard}>
                    R$ 41,99
                    </button>
                </a>
            </li>

            <li className={style.gamesectionlist}>
                <Image className={style.gameimg} src="https://assets.nuuvem.com/image/upload/t_product_sharing_banner/v1/products/557dbb9f69702d0a9c7da700/sharing_images/nok69j6m12kgovgokrbh.jpg" width={220} height={110} alt="Imagem gamecard" />
                <p className={style.titlegamecard}>
                    Batman Arkham
                </p>
                <div className={style.iconsection}>
                    <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                    <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                </div>

                <a href="/gamePageContent">
                    <button className={style.buttongamecard}>
                    R$ 41,99
                    </button>
                </a>
            </li>

            <li className={style.gamesectionlist}>
                <Image className={style.gameimg} src="https://assets.nuuvem.com/image/upload/t_product_sharing_banner/v1/products/557dbb9f69702d0a9c7da700/sharing_images/nok69j6m12kgovgokrbh.jpg" width={220} height={110} alt="Imagem gamecard" />
                <p className={style.titlegamecard}>
                    Batman Arkham
                </p>
                <div className={style.iconsection}>
                    <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                    <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                </div>

                <a href="/gamePageContent">
                    <button className={style.buttongamecard}>
                    R$ 41,99
                    </button>
                </a>
            </li>            

        </ul>
    );
}