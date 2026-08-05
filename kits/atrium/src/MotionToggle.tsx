export interface MotionToggleProps {
  /** True when the motion this control governs is stopped. */
  paused: boolean;
  onChange: (paused: boolean) => void;
  /** Names what it stops — "Logo rail", "Condition marquee". */
  controls?: string;
  className?: string;
}

/**
 * The visible off switch every autonomous motion in this pack ships with. It is
 * a component of the pack rather than an accessibility afterthought:
 * `prefers-reduced-motion` does not discharge the requirement, because the
 * people who most need to stop a marquee are frequently not the people who set
 * that flag.
 *
 * The control itself never moves, so it crosses into this kit even though the
 * motion it pauses does not. Wire `onChange` to whatever the pack's motion layer
 * is doing; the button is the whole of what the design system owns.
 */
export function MotionToggle({ paused, onChange, controls, className }: MotionToggleProps) {
  return (
    <button
      type="button"
      className={['at-motion-toggle', className].filter(Boolean).join(' ')}
      aria-pressed={paused}
      onClick={() => onChange(!paused)}
    >
      {/* Sentence case in the DOM, uppercased by the mono furniture rule: the
          label reads PAUSE MOTION and the accessible name stays a sentence. */}
      {paused ? 'Play motion' : 'Pause motion'}
      {controls !== undefined && <span className="at-motion-toggle__target">{controls}</span>}
    </button>
  );
}
