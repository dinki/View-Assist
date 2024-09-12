import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Bring Your Own Device',
    Svg: require('@site/static/img/undraw_devices.svg').default,
    description: (
      <>
         Android tablet, Wyoming satellite, ESPHome, PC, phone, or any other device, 
         integrate them all with Home Assistant's voice assistant quickly with View Assist.
      </>
    ),
  },
  {
    title: 'Build Your Own Experience',
    Svg: require('@site/static/img/undraw_add_information.svg').default,
    description: (
      <>
        Customizable and capable of integrating with existing dashboards, View Assist 
        lets you pick and use only the pieces you need.
      </>
    ),
  },
  {
    title: 'Extend Your Voice',
    Svg: require('@site/static/img/undraw_collaborators_re_hont.svg').default,
    description: (
      <>
        Use ready-made custom sentences, blueprints and views to enhance your voice powered
        Home Assistant experience.
      </>
    ),
  },
  {
    title: 'Create a Network',
    Svg: require('@site/static/img/undraw_having_fun.svg').default,
    description: (
      <>
        Create a network of satellite devices which will allow you to broadcast messages, display alaerts and more!
      </>
    ),
  },  
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
