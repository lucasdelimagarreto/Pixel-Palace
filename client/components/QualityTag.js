import Link from "next/link";
import Image from "next/image";
import imgQuality from "../assets/seloQualidade.png"

const QualityTag = () => (
    <section id="sectionImgSeloQualidade">
        <Image src={imgQuality} height={60} width={800} alt="pegie"/>
    </section>
);

export default QualityTag;