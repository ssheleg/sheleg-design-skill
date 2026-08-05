export interface Authority {
  id: string;
  name: string;
  /** The second line the name borrows its weight from. Never omitted. */
  institution: string;
  /** An optional third line: the role, the credential, the specialty. */
  role?: string;
}

export interface AuthorityRowProps {
  people: Authority[];
  /** Names the rail for assistive tech — "Our medical and scientific board". */
  label?: string;
  className?: string;
}

/**
 * Sourced authority as layout: named experts, each with their institution on a
 * second line. A claim without an attributed name is a ban in this pack, and
 * the institution line is also what keeps the section from reading as marketing.
 *
 * The rail scroll-snaps horizontally and is swipeable on touch. The pack's
 * desktop nav buttons are an affordance over that scroll, not the mechanism, so
 * they stay in the pack with the rest of the interaction.
 */
export function AuthorityRow({ people, label, className }: AuthorityRowProps) {
  return (
    <ul
      className={['at-authority', className].filter(Boolean).join(' ')}
      aria-label={label}
    >
      {people.map((person) => (
        <li key={person.id} className="at-authority__item">
          <span className="at-authority__name">{person.name}</span>
          <span className="at-authority__institution">{person.institution}</span>
          {person.role !== undefined && (
            <span className="at-authority__role">{person.role}</span>
          )}
        </li>
      ))}
    </ul>
  );
}
