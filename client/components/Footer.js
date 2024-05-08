import imgLogo from "../assets/logoPixelPalace.png"
import imgSocialMidias from "../assets/redesSociais.png"
import Image from "next/image";
import style from "../styles/footer.module.css"

const Footer = () => (
    <footer>
        <div id={style.divFooterFolowUs}>
            <p><strong>Siga a </strong>Pixel Palace</p>
            <Image src={imgSocialMidias} alt="" height={26} id={style.imgRedesSociais}/>
            <a href="" id={style.aFooterSobre}>Sobre</a>
        </div>
        <div id={style.divFooterLogo}>
            <Image src={imgLogo} alt="" height={120}/>
            <p id={style.pFooterSince}>©2024</p>
        </div>
        <div id={style.divFooterAddress}>
            <p class={style.pAddress}><strong class={style.colorWhite}>Pixel Palace</strong> Ltda.-CNPJ 17.126.332/0001-10<br/> Rua Lauro Müller, nº116, sala 503 - Torre do Rio Sul - Botafogo - Rio de Janeiro, RJ - 22290-160</p>
        </div>
    </footer>
);

export default Footer;