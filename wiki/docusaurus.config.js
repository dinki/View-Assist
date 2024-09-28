// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';
import tailwindPlugin from './plugins/tailwind-plugin.cjs';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'View Assist',
  tagline: 'Adding visual feedback and extended functionality to Home Assistant voice',
  favicon: 'img/favicon.png',

  // Set the production url of your site here
  url: 'https://dinki.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/View-Assist/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'dinki', // Usually your GitHub org/user name.
  projectName: 'View-Assist', // Usually your repo name.
  deploymentBranch:'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  headTags: [
    {
      tagName: 'link',
      attributes: {
        rel: 'preconnect',
        href: 'https://fonts.googleapis.com'
      }
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'preconnect',
        href: 'https://fonts.gstatic.com',
        crossorigin: 'anonymous'
      }
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap'
      }
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,300..900;1,300..900&family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap'
      }
    }
  ],

  plugins: [tailwindPlugin],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //  'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //  'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/ViewAssist-social-card.png',
      navbar: {
        title: 'View Assist',
        logo: {
          alt: 'View Assist Logo',
          src: 'img/view-assist.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Docs',
          },
          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/dinki/View-Assist',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'View Assist Setup',
                to: '/docs/viewassist-setup',
              },
              {
                label: 'Extend Voice Functionality',
                to: '/docs/extend-functionality',
              }
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'View Assist Discord',
                href: 'https://discord.gg/3WXXfGAf8T',
              },
              {
                label: 'View Assist Discussions',
                href: 'https://github.com/dinki/View-Assist/discussions',
              },              
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'View Assist GitHub',
                href: 'https://github.com/dinki/View-Assist',
              },
            ],
          },
        ],
        copyright: `<p>Find View Assist useful? Consider showing your support: <a href="https://www.buymeacoffee.com/dinki" rel="nofollow"><br \><br \><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" id="buyMeACoffee"></a></p> Copyright © ${new Date().getFullYear()} View Assist`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
