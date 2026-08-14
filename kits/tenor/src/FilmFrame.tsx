export interface FilmFrameProps {
  /** Source of a silent, looping product recording. */
  src: string;
  /** Required: it describes what the recording shows, and it is not decoration. */
  label: string;
  /** The frame's fill behind a letterboxed recording. */
  tone?: 'light' | 'dark';
  poster?: string;
  className?: string;
}

/**
 * Product proof, and in this pack it is never a screenshot: a silent looping
 * video in a 16:9 box with a 1px hairline and no radius.
 *
 * `muted` and `playsInline` are set here AND expected to be re-applied by the
 * page's own observer before play() — the reference does both, because a browser
 * that drops the attribute refuses autoplay silently.
 *
 * The component does not start playback. Gate it from the page with an
 * IntersectionObserver and pause it under reduced motion; a kit is the static
 * half of a pack and does not own the page's motion policy.
 */
export function FilmFrame({ src, label, tone = 'light', poster, className }: FilmFrameProps) {
  return (
    <div className={['tn-film', `tn-film--${tone}`, className].filter(Boolean).join(' ')}>
      <video
        className="tn-film__video"
        aria-label={label}
        poster={poster}
        muted
        loop
        playsInline
        preload="metadata"
      >
        <source src={src} type="video/mp4" />
      </video>
    </div>
  );
}
