/**
 * The six stops of `ctaCycle`, in the order it plays them. Stop 2 is the
 * darkest and therefore the pack's contrast floor; stop 5 is the lightest.
 */
export type Stop = 1 | 2 | 3 | 4 | 5 | 6;

export interface FieldStopProps {
  stop?: Stop;
  children?: import('react').ReactNode;
  className?: string;
}

/**
 * One named stop of the field cycle, rendered **static**.
 *
 * The cycle itself does not cross into a design system: a kit is the static
 * half of a pack, and motion stays behind in the pack. What crosses is the six
 * stops as six surfaces, so a design agent can lay a screen out against the
 * real extremes instead of against one representative pink.
 *
 * Build against stop 2 when you need to prove contrast — every ratio the pack
 * claims is stated there, because it is the worst of the six.
 */
export function FieldStop({ stop = 1, children, className }: FieldStopProps) {
  return (
    <div
      className={['cy-field', `cy-field--${stop}`, className].filter(Boolean).join(' ')}
      data-stop={stop}
    >
      {children}
    </div>
  );
}
