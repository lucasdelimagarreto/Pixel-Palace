import Image from "next/image";
import imgQuality from "../../assets/seloQualidade.png"
import style from "./qualityTag.module.css"

const QualityTag = () => (
    <section id={style.sectionImgSeloQualidade}>
        <Image src={imgQuality} height={60} width={800} alt="pegie"/>
    </section>
);

export default QualityTag;